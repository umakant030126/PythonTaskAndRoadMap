# 📅 Day 1 – Absolute Basics
# Print "Hello World"



def printSomeMessage(message):
    print(message)


# Swap two variables (without third variable)

def swapNumbers(n1, n2):
    print(n1 , n2)
    n1 = n1 * n2
    n2 = int(n1 / n2)
    n1 = int(n1 / n2)
    return n1,n2



# Check if a number is even or odd
def checkOddEven(number):
    if number % 2 == 0:
        print("Even")
    else:
        print("Odd")



# Find largest of 3 numbers
def maxInThreeNumbers(n1,n2,n3):
    return max(n1,n2,n3)


# Reverse a number
def reverseOfNumber(number):
    rev_num = 0
    while number:
        rev_num = (rev_num * 10) + number % 10
        number = number // 10
    return rev_num




# Count digits in a number
def countDigitInNumber(number):
    count = 0
    while number:
        number = number // 10
        count +=1
    return count


# Sum of digits
def sumOfDigits(number):
    sum = 0
    while number:
        sum = sum + (number % 10)
        number = number // 10
    return sum



# Check palindrome number
def checkPalindrome(number):
    rev_num = 0
    num = number
    while number:
        rev_num = (rev_num * 10) + number % 10
        number = number // 10

    if num == rev_num:
        return True
    else:
        return False



# Find factorial using loop
def getFatorialValue(num):
    factVal = 1
    for i in range(1,num+1):
        factVal = factVal *i

    return factVal



# Fibonacci series (n terms)
def printFibonacciSerise(n1 , n2 , nn ):
    print(n1 , n2)
    nextnum = n1 + n2
    print(nextnum)
    while (nn > nextnum):
        print(nextnum)
        n1 = n2
        n2 = nextnum
        nextnum = n1 + n2


printFibonacciSerise(0,1,15)



# 📅 Day 2 – Numbers + Logic
# Check prime number (optimized)
# Find all divisors of a number
# Check perfect number
# Convert binary to decimal
# Convert decimal to binary
# Find power using recursion
# GCD of two numbers
# LCM of two numbers
# Armstrong number
# Sum of natural numbers