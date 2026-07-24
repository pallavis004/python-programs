numbers = [25, 10, 45, 5, 30]
smallest = numbers[0]
for i in numbers:
    if i < smallest:
        smallest = i
print("Smallest =", smallest)