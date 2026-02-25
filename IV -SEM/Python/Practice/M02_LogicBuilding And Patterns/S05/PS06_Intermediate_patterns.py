"""li = [1,2,3,4,5]
res = []
for i in li:
    res.append(i ** 2)
print(res)

ans = [i ** 2 for i in li]
print(ans)"""

"""print(" * "*5)
li = ['a', 'b', 'c']
res = ""
for ch in li:
    res = res + ch + " "
print(res)

print("@".join(li))"""

"""n = int(input())
for i in range(1, n+1):
    print(" "*(n-i) + "* "*i)
print("-----------------")
for i in range(n,0,-1):
    print(" "*(n-i)+"* "*i)
    """
"""n = int(input())
for i in range(1, n+1):
    print(" "*(n-i)+" ".join([str(j) for j in range(1, i+1)]))"""
#Hollow Pyramid
n=int(input())
for i in range(1,n+1):
    if i == 1:
        print(" "*(n-i)+"*")
    else:
        print(" "*(n-i)+"*"+" "*(2*i-3)+"*")