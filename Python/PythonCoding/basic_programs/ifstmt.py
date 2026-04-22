"""
Date : 22-04-2026
"""
#big2

'''
num1 = int(input('Enter 1st number:'))
num2 = int(input('Enter 2nd number:'))

if num1 == num2:
    print('Both are equal')
elif num1 > num2 :
    print(num1 , 'is big')
else:
    print(num2 , 'is big')
'''

#big3

'''num1 = int(input('Enter 1st Number :'))
num2 = int(input('Enter 2nd number :'))
num3 = int(input('Enter 3rd Number :'))

if num1 == num2 and num2 == num3 :
    print('All values are equal')
elif num1 > num2 and num1 > num3:
    print(num1 , 'num1 is greater')
elif num2 > num1 and num2 > num3:
    print(num2 , 'num2 is greater')
elif num3 > num1 and num3 > num2:
    print(num3 , 'num3 is greater')
'''

ch = int(input('Enter a number bet 1-7 :'))

match(ch):
    case 1:
        print('Monday')
    case 2:
        print('Tuesday')
    case 3:
        print('Wednesday')
    case 4:
        print('Thursday')
    case 5:
        print('Friday')
    case 6:
        print('Saturday')
    case 7:
        print('Sunday')
    case _:
        print('Invalid Choice')