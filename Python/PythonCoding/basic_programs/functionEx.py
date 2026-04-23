
#function part

'''def add(a,b):
    return a+b
#Driver code
result = add(10,20)
print(result)'''

numbers = [1,2,3,4,5]
sq = lambda nums : [num * num for num in nums]
print(tuple(sq(numbers)))