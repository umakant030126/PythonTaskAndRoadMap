from collections import Counter

## Day 4
# 16. Anagram check
str1 = "abbdfcrcdef"
str2 = "defabbdfcrc"
lst1 = []
lst2 = []
for char in str1:
    lst1.append(char)

for char in str2:
    lst2.append(char)

lst1.sort()
lst2.sort()

if lst1 == lst2:
    print("Its Anagram.")
else:
    print("Its not Anagram.")



# 17. First non-repeating char
def find_nonRepeatedChar(input_str):
    counts = Counter(input_str)
    return counts

charCount = dict(find_nonRepeatedChar("apple banana mango"))
print(charCount)
for ch in charCount:
    cnt = charCount.get(ch)
    if cnt == 1:
        print(ch)
        break



# 18. Capitalize words
str3 = "apple banana mango"
print(str3.title())
print(str3.capitalize())

# 19. Character frequency
str4 = "apple banana mango orange"
def charFrequency(inputString):
    counts = Counter(inputString)
    return counts

feq_count = dict(charFrequency(str4))
print(feq_count.items())

# 20. Replace substring
str5 = "I love Java and learning Java."
print(str5.replace("Java", "Python"))
