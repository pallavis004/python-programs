text = input("Enter a string: ")
letter = input("Enter a letter: ")
if text.startswith(letter):
    print("The string starts with", letter)
else:
    print("The string does not start with", letter)