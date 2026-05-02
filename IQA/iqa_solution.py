# FOUNDATION + THINKING LIKE DEV
# 📅 Day 1 – Basic Input/Output & Conditions
#
# Scenario: Startup Employee System
#
#     Take employee name & salary → classify tax slab
# emp_name = input("Enter employee name :")
# emp_salary = float(input("Enter employee salary"))
import random


def employeeTaxSlab(name, salary):
    package = 12 * salary
    if package < 500000:
        print(f"{name}, you are in 5% tax slab.")
    elif (package >= 500000) and (package < 1000000):
        print(f"{name}, you are in 10% tax slab.")
    elif (package >= 1000000) and (package < 1500000):
        print(f"{name}, you are in 15% tax slab.")
    elif (package >= 1500000) and (package < 2000000):
        print(f"{name}, you are in 20% tax slab.")
    else:
        print(f"{name}, you are in 30% tax slab.")


# employeeTaxSlab(emp_name,emp_salary)


#     Check if employee ID is valid (numeric + length)
def checkEmployeeID(empId):
    if len(empId) != 8:
        print(f"Employee ID is {empId}, and it's invalid. Employee ID length should be 8 char")
    elif empId[0:3].isalpha() and empId[3:].isdigit():
        print(f"{empId} is valid employee ID")
    else:
        print(f"{empId} is invalid employee ID")

# checkEmployeeID("EMP12345")
# checkEmployeeID("EMP1235")
# checkEmployeeID("EMPS2345")
# checkEmployeeID("EMP54512345")


#     Bonus eligibility based on performance score
def bonusEligibility(rating):
    if rating == 1:
        print(f"your rating is {rating}. This means, low performance. So no Bonus this year...!")
    elif rating == 2:
        print(f"your rating is {rating}. This means, below average performance. So 5% Bonus this year...!")
    elif rating == 3:
        print(f"your rating is {rating}. This means, Average performance. So 10% Bonus this year...!")
    elif rating == 4:
        print(f"your rating is {rating}. This means, Good performance. So 25% Bonus this year...!")
    elif rating == 5:
        print(f"your rating is {rating}. This means, Excellent performance. So 50% Bonus this year...!")
    else:
        print(f"{rating} is invalid rating. Maximum rating is 5.")

# bonusEligibility(1)
# bonusEligibility(2)
# bonusEligibility(3)
# bonusEligibility(4)
# bonusEligibility(5)
# bonusEligibility(6)

#     Compare 3 employees salary → highest
def getHighestsalary(a,b,c):
    return c if c > (a if a>b else b) else (a if a>b else b)

# print(getHighestsalary(100,300,200))
# print(getHighestsalary(1000,300,200))
# print(getHighestsalary(100,300,2000))


#     Login system (username/password match)
user_name = "ukp"
password = 'pku'

flag_val = True
count = 0
max_attempt = 3
while (flag_val or count <= 3):
    un = input("Enter user name : ")
    up = input("Enter password : ")
    if ((un != user_name) or (up != password)):
        count += 1
        max_attempt = max_attempt - 1
        print(f"username or password is invalid, please try again. You have {max_attempt} left.")
        if max_attempt == 0:
            break
    else:
        print(f"Welcome {un}")
        break



#     ATM withdrawal validation
bal_amt = 1000
def checkWithDrawAmount(withdraw_amount):
    global bal_amt
    if withdraw_amount < bal_amt:
        bal_amt = bal_amt -withdraw_amount
        print(f"you can withdraw {withdraw_amount} after this you have {bal_amt}")
    else:
        print(f"You have not sufficient balance. You have {bal_amt}")

# checkWithDrawAmount(500)
# checkWithDrawAmount(300)
# checkWithDrawAmount(400)


#     Check if number is positive/negative/zero
def checkNumberSign(number):
    if number >= 1:
        print(f"Number is {number}. it's Positive number.")
    elif number == 0:
        print(f"Number is {number} and have no sign. it's zero.")
    else:
        print(f"Number is {number}. it's Negative number.")

# checkNumberSign(0)
# checkNumberSign(-22)
# checkNumberSign(22)
# checkNumberSign(332)
# checkNumberSign(-3333)


# 📅 Day 2 – Loops (Real Automation)
#
# Scenario: Log Monitoring Tool


#     Count error logs
def getErrorCount(filename, mode):
    error_count = 0
    with open(filename, mode) as fd:
        lines = fd.readlines()
        for line in lines:
            if line.__contains__("DEBUG"):
                error_count += 1
    return error_count

# print(getErrorCount("logs.txt","rt"))


#     Print first 50 log entries
def getNLinesOfLogs(filename,mode, number_of_lines):
    count = 0
    with open(filename,mode) as fd:
        lines = fd.readlines()
        for line in lines:
            if count < number_of_lines:
                print(line)
                count +=1

# getNLinesOfLogs("logs.txt","rt",5)


#     Find repeated logs
def getDuplicateItemInList(list_name):
    seen = set()
    duplicate_set = set()
    for item in list_name:
        if item in seen:
            duplicate_set.add(item)
        else:
            seen.add(item)
    return duplicate_set

def getRepeatedLogData(filename, mode):
    with open(filename, mode) as fd:
        lst_data = []
        lines = fd.readlines()
        for line in lines:
            if line.__contains__("LOGID"):
                lst_data.append(line[(line.find('LOGID')+len("LOGID")+6):])

        lst =  list(getDuplicateItemInList(lst_data))
        lst_op = []
        for single_item in lines:
            if single_item.__contains__(lst[0]):
                lst_op.append(single_item)

        return lst_op


print(getRepeatedLogData("logs.txt","rt"))




#     Count digits in log ID



def getDigitCountInLogId(logId):
    count = 0
    for ch in logId:
        if ch.isdigit():
            count += 1
    return count

count = getDigitCountInLogId("CIDXI-258749631")

# print(f" Digits count in LogId is {count}")

#     Reverse log ID

def getReversedLogId(logId):
    return logId[-1::-1]

print(getReversedLogId("ABCD_1234"))


#     Generate request IDs sequence
def gererateRequestId():
    return "REQ-" + str(random.randint(1000,9999))

print(gererateRequestId())

# 📅 Day 3 – Strings (Text Processing 🔥)
#
# Scenario: Chat Application
#
#     Count words in message
#     Detect spam words
#     Reverse message
#     Check palindrome message
#     Replace bad words with ***
#     Find most frequent word
#     Remove duplicate characters
#     Check anagram messages
#     Extract hashtags
#     Count emojis (basic pattern)
#
# 📅 Day 4 – Lists (Data Handling)
#
# Scenario: E-commerce Cart
#
#     Add/remove items
#     Find most expensive item
#     Apply discount on all items
#     Remove duplicate items
#     Sort items by price
#     Merge two carts
#     Find common items
#     Count item frequency
#     Split cart into categories
#     Flatten nested cart
#
# 📅 Day 5 – Dictionaries (🔥 Real Use)
#
# Scenario: User Database
#
#     Store user details
#     Update user email
#     Find user by ID
#     Count users per city
#     Sort users by age
#     Merge two user DBs
#     Remove inactive users
#     Find duplicate emails
#     Convert list → dict
#     Nested dict traversal
#
# 📅 Day 6 – Functions
#
# Scenario: Utility Library
#
#     Function for tax calculation
#     Function to validate email
#     Function for password strength
#     Recursive factorial
#     Recursive Fibonacci
#     Function to find max in list
#     Function returning multiple values
#     Lambda for sorting
#     Function with *args
#     Function with **kwargs
#
# 📅 Day 7 – Mini Project 🔥
#
# Scenario: CLI-Based Student Management
#
#     Add student
#     Delete student
#     Update marks
#     Calculate average
#     Grade system
#     Search student
#
# 🟡 WEEK 2 (Day 8–14) → INTERMEDIATE CORE
#
# 📅 Day 8 – List Comprehension + Functional
#
# Scenario: Data Cleaning Tool
# (10 problems: filtering, mapping, transformations)
#
# 📅 Day 9 – Sets & Advanced Collections
#
# Scenario: Fraud Detection
# (duplicates, intersections, unique patterns)
#
# 📅 Day 10 – File Handling
#
# Scenario: Log Analyzer
#
#     Count errors
#     Extract IPs
#     Find top errors
#
# 📅 Day 11 – Exception Handling
#
# Scenario: Payment Gateway
#
#     Handle failed transactions
#     Retry logic
#
# 📅 Day 12 – OOP Basics 🔥
#
# Scenario: Bank System
#
#     Account class
#     Deposit/withdraw
#     Balance check
#
# 📅 Day 13 – OOP Advanced
#     Inheritance (Savings/Current Account)
#     Method overriding
#     Encapsulation
#
# 📅 Day 14 – Mini Project 🔥
#
# Build: Banking System CLI App
#
# 🔴 WEEK 3 (Day 15–21) → DSA + INTERVIEW CORE
# 📅 Day 15 – Searching & Sorting
#     Search products
#     Sort orders
#
# 📅 Day 16 – Strings Advanced 🔥
#     Longest substring
#     String compression
#
# 📅 Day 17 – Arrays (🔥 MOST ASKED)
#     Two Sum
#     Move zeros
#     Rotate array
#
# 📅 Day 18 – Hashing
#     Frequency maps
#     Subarray sum
#
# 📅 Day 19 – Stack & Queue
#     Browser history
#     Undo feature
#
# 📅 Day 20 – Linked List
#     Reverse list
#     Detect cycle
#
# 📅 Day 21 – Mini Project 🔥
#
# Build: Task Scheduler (Queue-based)
#
# ⚫ WEEK 4 (Day 22–30) → ADVANCED + INTERVIEW DOMINATION
# 📅 Day 22 – Recursion & Backtracking
#     Permutations
#     Subsets
#
# 📅 Day 23 – Sliding Window 🔥
#     Max sum subarray
#     Longest substring
#
# 📅 Day 24 – Heaps & Priority Queue
#     Top K elements
#     Task priority system
#
# 📅 Day 25 – Decorators 🔥
#     Logging decorator
#     Auth decorator
#
# 📅 Day 26 – Generators
#     Infinite streams
#     Lazy loading
#
# 📅 Day 27 – Multithreading
#     Parallel tasks
#     File processing
#
# 📅 Day 28 – System Design Lite
#
# Scenario: URL Shortener (logic only)
#
# 📅 Day 29 – Final Project 🔥🔥🔥
#
# Build: E-commerce Backend (CLI version)
#
#     Users
#     Orders
#     Cart
#     Payments
#
# 📅 Day 30+ – DSA
#     Solve 5 random problems
#     Explain approach
#     Optimize solution