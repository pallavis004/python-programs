numbers = [1, 2, 3, 2, 4, 2, 5]
num = int(input("Enter the number to count: "))
count = 0
for i in numbers:
    if i == num:
        count = count + 1
print("Frequency =", count)