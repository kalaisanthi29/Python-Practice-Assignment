# Exercise 1: Greeting and Age Check
name = input("Enter your name: ")
age = int(input("Enter your age: "))

if age >= 18:
    print(f"Hi {name}, you can enter!")
else:
    print(f"Sorry {name}, you're too young.")

# Exercise 2: Number List Processor
n = int(input("\nEnter a number: "))
numbers = []

for i in range(1, n + 1):
    numbers.append(i)

print(numbers)

if n > 5:
    print("The list is long.")
else:
    print("The list is short.")

# Exercise 3: Sum of User Inputs
num1 = int(input("\nEnter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

number_list = [num1, num2, num3]
total = num1 + num2 + num3

print("Numbers:", number_list)
print("Total:", total)

if total % 2 == 0:
    print("Your sum is even!")
else:
    print("Your sum is odd!")

# Exercise 4: Fruit Basket
fruits = {
    "apple": 10,
    "banana": 5,
    "orange": 8
}

fruit_name = input("\nEnter a fruit name: ").lower()

if fruit_name in fruits:
    print(f"We have {fruits[fruit_name]} {fruit_name}(s).")
    for letter in fruit_name:
        print(letter)
else:
    print("We don't have that fruit.")


# Exercise 7: Number Analyzer
user_input = input("\nEnter numbers separated by spaces: ")
string_numbers = user_input.split()

numbers = []
for item in string_numbers:
    numbers.append(int(item))

print("Numbers:", numbers)

smallest = numbers[0]
largest = numbers[0]
total = 0

for num in numbers:
    if num < smallest:
        smallest = num
    if num > largest:
        largest = num
    total += num

average = total / len(numbers)

print("Smallest:", smallest)
print("Largest:", largest)
print("Average:", average)

if average > 10:
    print("Average is high")
else:
    print("Average is low")


# Exercise 10: Shopping List Manager
shopping_list = []

while True:
    item = input("\nEnter an item to add (or type 'done'): ")

    if item.lower() == "done":
        break
    else:
        shopping_list.append(item)

print("Shopping list:", shopping_list)

if len(shopping_list) > 3:
    print("You have a lot of items!")
else:
    print("You have a short list.")
    