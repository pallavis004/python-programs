def check_number(num):
    if num > 0:
        return "Positive Number"
    elif num < 0:
        return "Negative Number"
    else:
        return "Zero"
number = float(input("Enter a number: "))
print(check_number(number))