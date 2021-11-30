# write your code here
import random
import time


def level_description(is_simple):
    if is_simple == 1:
        return "1 (simple operations with numbers 2-9)"
    elif is_simple == 2:
        return "2 (integral squares 11-29)"


class Exam:
    def __init__(self):
        self.num1 = None
        self.num2 = None
        self.num3 = None
        self.my_operator = None
        self.answer = None
        self.result = 0
        self.mark = 0

    def simple(self):
        self.num1 = random.randint(2, 9)
        self.num2 = random.randint(2, 9)
        self.my_operator = random.choice(["+", "-", "*"])
        print(f"{self.num1} {self.my_operator} {self.num2}")
        self.execution()

    def execution(self):
        if self.my_operator == "+":
            self.result = self.num1 + self.num2
        elif self.my_operator == "-":
            self.result = self.num1 - self.num2
        elif self.my_operator == "*":
            self.result = self.num1 * self.num2
        self.input_validation()

    def input_validation(self):
        status = True
        while status:
            try:
                self.answer = int(input())
            except ValueError:
                print("Incorrect format.")
                status = True
            else:
                break

    def not_simple(self):
        self.num3 = random.randint(11, 29)
        print(self.num3)
        self.result = self.num3 ** 2
        self.input_validation()

    def level(self):
        while True:
            try:
                choice = int(input("""Which level do you want? Enter a number:
        1 - simple operations with numbers 2-9
        2 - integral squares of 11-29\n"""))
            except ValueError:
                print("Incorrect format.")
            else:
                break
        if choice == 1:
            return 1
        elif choice == 2:
            return 2
        elif choice != 1 and choice != 2:
            print("Incorrect format.")

    def grading(self):
        if self.answer == self.result:
            print("Right!")
            self.mark += 1
        else:
            print("Wrong!")

    def save_result(self,level):
        save_input = input("Would you like to save the result? Enter yes or no.")
        if save_input in ["yes", "YES", "y", "Yes"]:
            file = open('results.txt', 'a')
            user_name = input("What is your name?\n")
            file.write(f'{user_name}: {self.mark}/5 in level {level}.\n')
            file.close()
            print('The results are saved in "results.txt".')

        elif save_input == "exit":
            exit()

    def main(self):
        is_simple = self.level()
        level_string = level_description(is_simple)
        for _ in range(5):
            if is_simple == 1:
                self.simple()
            elif is_simple == 2:
                self.not_simple()

            self.grading()

        print(f"Your mark is {self.mark}/5.")
        self.save_result(level_string)

if __name__ == '__main__':
    Exam().main()

