import random


# 1.
try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ZeroDivisionError:
    print("You cannot divide by zero.")

# 2.
try:
    length = int(input("Enter the length of the list: "))
    my_list = list(range(length))
    index = random.randint(0, length + 1)
    print("Element at random index:", my_list[index])
except IndexError:
    print("Index out of range.")

# 3.
try:
    user_input = input("Enter a number to convert to integer: ")
    number = int(user_input)
except ValueError:
    print("Invalid number!")

# 4.
filename = "example.txt"
try:
    with open(filename, "r") as file:
        content = file.read()
except FileNotFoundError:
    with open(filename, "w") as file:
        file.write("New file created.")
    print(f"{filename} not found. A new file has been created.")

# 5.
try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("Difference:", a - b)
finally:
    print("Calculation completed.")

# 6.
try:
    numerator = int(input("Enter numerator: "))
    denominator = int(input("Enter denominator: "))
except ValueError:
    print("Invalid input!")
else:
    try:
        print("Result:", numerator / denominator)
    except ZeroDivisionError:
        print("Cannot divide by zero.")

# 7.
my_dict = {"a": 1, "b": 2, "c": 3}
key = input("Enter a dictionary key: ")
try:
    print("Value:", my_dict[key])
except KeyError:
    print("Key not found in dictionary.")

# 8.
file_lines = ["10", "abc", "30"]
for line in file_lines:
    try:
        num = int(line)
        print("Number:", num)
    except ValueError:
        print("Error")

# 9.
data = ["1", "2", "3"]
try:
    int_list = [int(x) for x in data]
except ValueError:
    print("Conversion failed.")
else:
    print("All conversions successful.")

# 10.
my_list = [1, 2, 3]
try:
    if not my_list:
        raise ValueError("List is empty")
    total = sum(my_list)
    print("Sum of list:", total)
except ValueError as e:
    print("Error:", e)
else:
    print("List operation successful.")
finally:
    print("Operation finished.")
