from collections import Counter

## Day 3
# 11. Reverse string
# str1 = input("Enter a String to reverse : ")
# str_len = len(str1)
# rev_str = str1[-1::-1]
# print(rev_str)


# 12. Palindrome string
# str2 = input("Enter a String to check, is it Palindrome or not ? -> ")
# revStr = str2[-1::-1]
# if str2 ==revStr:
#     print(f"You entered '{str2}' and it's Palindrome.")
# else:
#     print(f"You entered '{str2}' and it's not Palindrome.")

# 13. Count vowels
# str3 = input("Enter a string to check how many vowel are there ? : ")
# vowelList = ['a','e','i','o','u','A','E','I','O','U']
# vowelCount = 0
# for char in str3:
#     if char in vowelList:
#         vowelCount += 1
# print(f'You entered "{str3}" and count of vowel in it is : {vowelCount}')

# 14. Remove spaces
# str4 = input("Enter a String : ")
# print(str4)
# str_withOutSpace = str4.replace(" ","")
# print(str_withOutSpace.strip())

# 15. Duplicate characters
str5 = input("Enter a String : ")


def find_duplicates(input_str):
    # Count frequency of each character
    counts = Counter(input_str)
    print(counts)
    # Extract characters that occur more than once
    return [char for char, count in counts.items() if count > 1]

print(find_duplicates(str5))


