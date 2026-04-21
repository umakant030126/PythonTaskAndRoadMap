
## Day 1
# 1. Print Hello World
print("Hello World")


# 2. Swap two variables
num1 = 10
num2 = 5
print(f'Before swap : {num1}')
print(f'Before swap : {num2}')

num1 = num1 * num2
num2 = num1 / num2
num1 = num1 / num2

print(f'After swap : {int(num1)}')
print(f'After swap : {int(num2)}')

# 3. Check even/odd

number = int(input("Enter a Integer num : "))
if number % 2 == 0:
    print(f"You enter {number} and it's even number")
else:
    print(f"You enter {number} and it's odd number")

# 5. Reverse number
number =  int(input("Enter a number with some digit: "))
print(f"Entered number is : {number}")
rev_num = 0

while number:
    rev_num = (rev_num * 10) + number % 10
    number = number // 10

print(f"Reverse number is : {rev_num}")