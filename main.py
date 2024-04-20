source_value = input("Enter the number you want to convert: ")
source_base = int(input("What is the base of your number? "))
desired_base = int(input("What base would you like to convert to? [2, 8, 10, 16] "))
precision_number = int(input("For fractions, what is the precision value? "))
print("Note: Binary  base10, base16, and base8 cannot use division")
conversion_method = int(input("Conversion method?: 1. Subtraction 2. Division 3. Multiplication [Enter 1,2,3] "))


def subtraction(v, d_base: int):
    value = int(str(v), 10)  # 190
    index = 10
    possible_digits = []
    rem = []
    helpme = []
    for power in range(index+1).__reversed__():
        compare_value = d_base**power

        if compare_value <= value:
            possible_digits.append(compare_value)
    # print(possible_digits)  # [32, 16, 8, 4, 2, 1]

    for i in possible_digits:

        answer = value - i
        value = answer
        if value > 0:
            rem.append(answer)

            helpme.append(1)
        else:

            helpme.append(0)
    helpme[-2] = d_base - 1

    for h in helpme:
        print(h, end=" ")


def division(n, d: int):  # baseX  Decimal  baseY
    try:
        int(str(n), 10)
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


def dec2hex_div(decimal_input):  # Special case
    temp_value = int(decimal_input, 10)
    hex_alphabet = "0123456789ABCDEF"
    if temp_value == 0:
        return "0"

    hexa = ""
    while temp_value > 0:
        remainder = temp_value % 16
        hexa = hex_alphabet[remainder] + hexa
        temp_value //= 16

    print(hexa)


def multiplication(v, d_base):
    try:
        rem = []
        temp_value = float(v)

        i, d = divmod(temp_value, 1)

        while d != 0:
            next_val = d * d_base
            i, d = divmod(next_val, 1)
            next_val = d * d_base
            rem.append(i)

        for digit in rem:
            print(int(digit), end=" ")
    except TypeError:
        print("Error ")



def bincasting(binary):
    input_casting = int(binary)
    base10, i, n = 0, 0, 0

    while input_casting != 0:
        dec = input_casting % 10
        base10 = base10 + dec * pow(2, i)
        input_casting = input_casting // 10
        i += 1
    return base10


def tempdeci2hex(n):
    rem = ['0'] * 100

    index = 0
    while n != 0:

        temp = 0

        temp = n % 16

        if temp < 10:
            rem[index] = chr(temp + 48)
            index = index + 1
        else:
            rem[index] = chr(temp + 55)
            index = index + 1
        n = int(n / 16)

    j = index - 1
    while j >= 0:
        print((rem[j]), end="")
        j = j - 1
    print()


def binToHexa(n):
    decimal = bincasting(n)
    print("Hexadecimal equivalent of {}: ".format(n))
    tempdeci2hex(decimal)


def binaryTodecimal(n):
    temp = int(n, 10)
    decimal = 0
    power = 1
    while temp > 0:
        rem = temp % 10
        temp = temp // 10
        decimal += rem * power
        power = power * 2

    return decimal


def menu():
    if source_base == 2 and desired_base == 16:
        binToHexa(str(source_value))
    elif source_base == 2 and desired_base == 10:
        print(binaryTodecimal(source_value))
    elif conversion_method == 1:
        subtraction(source_value, desired_base)
    elif conversion_method == 2 and desired_base == 2 or desired_base == 8:
        division(int(source_value), desired_base)
    elif conversion_method == 2 and desired_base == 16:
        dec2hex_div(source_value)
    elif conversion_method == 3:

        multiplication(source_value, desired_base)


menu()

