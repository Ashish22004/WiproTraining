# 1. Find the sum of numbers from 1 to 50 using xrange

total = 0
for i in range(1,51):
    total = total + i
print('the sum of numbers from 1 to 50 is :' ,total)

# 2. Count how many times "a" appears in a string using enumerate.

text = input("Enter a String :")
count = 0
for index, char in enumerate(text):
    if char == 'a':
        count = count+1
print('Number of a =' , count)