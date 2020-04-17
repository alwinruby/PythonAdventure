'''
Take the 3 digit number and split into each digit
'''
Number = 987
print(Number)
First = int(Number/100)
print(First)
#print(Number)
Number = Number-First*100
#print(Number)
Second = int(Number/10)
print(Second)
#print(Number)
Third = Number-Second*10
print(Third)
#print(Number)