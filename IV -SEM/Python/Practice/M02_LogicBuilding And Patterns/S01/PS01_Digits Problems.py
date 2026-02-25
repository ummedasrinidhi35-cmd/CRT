"""n=int(input())
count=0
while n>0:
    n=n//10
    count+=1
print(count)
"""
"""
n=int(input())
s=0
while n>0:
    r=n%10
    s+=r
    n=n//10
print(s)
""" 
""" 
n=int(input()) #to find the even digits in a given number

while n>0:
    r=n%10
    if r%2==0:
        print(r, end="")
    n=n//10
    """
      
  
"""
n=int(input()) #to find the reverse of a given number
rev=0
while n>0:
    r=n%10
    rev=rev*10+r
    n=n//10
print(rev)
"""
"""def reverse(num):
    rev=0
    while num>0:
        r=num%10
        rev=rev*10+r
        num=num//10
    return rev
n=reverse(int(input()))
while n>0:
    r=n%10
    if r%2==0:
        print(r, end="")
    n=n//10
    """
n=int(input()) # to check whether the given  number is palindrome or not
temp=n
rev=0
while n>0:
    r=n%10
    rev=rev*10+r
    n=n//10
if temp==rev:
    print(True)
else:
    print(False)
#check Armstrong number
#count even and odd digits
#Find largest  and smallest digit
#count Zero digits
#Find digital root of a number
#check spy number


    

        
    
 