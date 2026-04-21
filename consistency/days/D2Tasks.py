## Day 2
from math import factorial

# 6. Palindrome number
num1 = int(input("Enter a number more than 2 digits : "))
initial_num = num1
rev_num = 0

while num1:
    rev_num = (rev_num * 10) + num1 % 10
    num1 =  num1 // 10

if initial_num == rev_num:
    print(f"Enter number is {initial_num} and it's palindrome.")
else:
    print(f"Enter number is {initial_num} and it's not palindrome.")


# 7. Count digits
num2 = int(input("Enter a number to count its digits : "))
input_num = num2
count = 0
while num2:
    count = count + 1
    num2 = num2 // 10

print(f"You entered {input_num} which have {count} length.")


# 8. Sum of digits
num3 = int(input("Enter a number to sum of its digits : "))
input_num = num3
sum = 0
while num3:
    sum = sum + num3 % 10
    num3 = num3 // 10

print(f"You entered {input_num} and sum of it's all digits is {sum}")


# 9. Factorial
num4 = int(input("Enter a number to get factorial value : "))
factorialVal = 1
if num4 == 1:
    print(f"You entered {num4} and its factorial value 1")
else:
    for i in range(1,(num4+1)):
        factorialVal = i * factorialVal

print(f"You entered {num4} and its factorial value {factorialVal}")

# 10. Fibonacci
first_num = 0
second_num = 1
last_num = int(input("Enter a integer to get its Fibonacci series"))

print(first_num)
print(second_num)
next_num = first_num + second_num
while last_num >= next_num:
    print(next_num)
    first_num = second_num
    second_num = next_num
    next_num = first_num + second_num





