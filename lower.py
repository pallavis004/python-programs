text = input("Enter a string: ")
upper = 0
lower = 0
for i in text:
    if i.isupper():
        upper = upper + 1
    elif i.islower():
        lower = lower + 1
print("Uppercase =", upper)
print("Lowercase =", lower)