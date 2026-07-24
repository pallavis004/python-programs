numbers = [10, 40, 20, 50, 30]
largest = second = numbers[0]
for i in numbers:
    if i > largest:
        second = largest
        largest = i
    elif i > second and i != largest:
        second = i
print("Second Largest =", second)