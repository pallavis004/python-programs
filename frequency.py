text = input("Enter a string: ")

frequency = {}

for i in text:
    if i in frequency:
        frequency[i] = frequency[i] + 1
    else:
        frequency[i] = 1

for i in frequency:
    print(i, "=", frequency[i])