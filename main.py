# Author: Homer
source_value = int(input("Enter the number you want to convert: "))
source_base = int(input("What is the base of your number? "))
desired_base = int(input("What base would you like to convert to? [2, 8, 10, 16]"))
precision_number = int(input("For fractions, what is the precision value? "))
conversion_method = int(input("Choose a conversion method: 1. Subtraction 2. Division 3. Multiplication [Enter 1,2,3]"))

if source_value < 0 or type(source_value) is float:
    print("Please DO NOT enter negative or float values. ")


def subtraction(value: int, base: int, d_base: int):
    pass


def division(n: int, d: int):
    try:
        remainder_storage = []
        temp = n // d
        temp_remainder = n % d
        remainder_storage.append(temp_remainder)
        while temp >= 1:
            result = temp // d
            remainder = temp % d
            temp = result
            remainder_storage.append(remainder)

        print(remainder_storage[::-1])
    except TypeError:
        print("Do NOT enter a float or negative Number")


def multiplication(value, base, d_base):
    pass


def menu():
    if conversion_method == 1:
        pass
    elif conversion_method == 2:
        division(source_value, desired_base)
    elif conversion_method == 3:
        pass






