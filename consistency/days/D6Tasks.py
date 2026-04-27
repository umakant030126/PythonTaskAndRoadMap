# 📅 DAY 6 (Strings + Basics)
# 26. Reverse words in a sentence
input_str = input("Enter a String : ")
words_lst = input_str.split(" ")
rev_words_lst = words_lst[::-1]
op_str = " ".join(rev_words_lst)
print(op_str)


# 27. Find length of string without len()

counter = 0
for i in input_str:
    counter = counter + 1

print(f"Length of entered string is : {counter}")

# 28. Remove duplicate characters from string
char_lst = []
print(input_str)
for ch in input_str:
    if ch in char_lst and ch != " ":
        continue
    else:
        char_lst.append(ch)

unique_char_str = "".join(char_lst)
print(unique_char_str)




# 29. Check if string contains only digits
boolVal = False
for ch in input_str:
    if ch.isdigit():
        boolVal = True
        break
    # else:
    #     print("No, Str do not contain Digit")
    #     continue
if boolVal == True:
    print("Yes, String contain digit")
else:
    print("No, String do not contain digit")



# 30. Count words in a sentence
words_lst = input_str.split(" ")
print(f"Word count is string is : {len(words_lst)}")

print("-------------------------------------------------------------------")
# 31. Check prime number (optimized)

def isPrimeNumber(num):
    if num< 2:
        return False

    d_count = 0
    for i in range(2,num):
        if num % i == 0:
            d_count +=1

    if d_count > 1:
        return False
    else:
        return True

print(isPrimeNumber(7))
print(isPrimeNumber(12))
print("-------------------------------------------------------------------")

# 32. Find all divisors of a number
number = int(input("Enter a Integer number : "))
divisor_lst = []
for i in range(1,number+1):
    if number % i == 0:
        divisor_lst.append(i)

print(divisor_lst)



# 33. Check perfect number
sum = 0
divisor_lst_exclude_num = []
for i in range(1,number):
    if number % i == 0:
        divisor_lst_exclude_num.append(i)

print(divisor_lst_exclude_num)
for num in divisor_lst_exclude_num:
    sum +=num

if sum == number:
    print(f"{number} is a Perfect number")
else:
    print(f"{number} is not a Perfect number")


# 34. Convert binary to decimal
'''
num=        1       0       1       1       0       0
indexes     0       1       2       3       4       5
neg_ind     -6      -5      -4      -3      -2      -1


    0                  0                        1                   1                      0                      1
<num_val>*2^0       <num_val>*2^1         <num_val>*2^2       <num_val>*2^3          <num_val>*2^4       <num_val>*2^5

'''


binary_num = int(input("Enter Binary number using 0 and 1 : "))
input_num = binary_num
binary_digits = []
decimal_num = 0
while binary_num:
    binary_digits.append(binary_num % 10)
    binary_num = binary_num // 10

print(f"enter number is {input_num}")
print(f"enter number is {binary_digits}")

for i in range(0,len(binary_digits)):
    decimalDigit = binary_digits[i] * pow(2,i)
    decimal_num = decimal_num + decimalDigit

print(f"Binary number is {input_num} and its decimal value is {decimal_num}")

# 35. Find power using recursion
def getPower(base,exponential):
    if exponential == 0:
        return 1
    else:
        return base * getPower(base, exponential-1)

(print(getPower(2,10)))
print(getPower(4,3))