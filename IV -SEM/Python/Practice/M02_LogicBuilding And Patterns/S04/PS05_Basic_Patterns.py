"""n=int(input())
for i in range(n):
    for j in range(n):
        print("*", end=" ") #used to print  he * in the same line
    print() #used to print the * in the next 
    """
#Right angled triangle
"""n=int(input())
for i in range(1, n+1):
    for j in range(i):
        print("*", end=" ")
    print()
"""
#Inverted Triangle
n=int(input())
for i in range(n):
    for j in range(n-i, 0, -1):
        print("*", end=" ")
    print()