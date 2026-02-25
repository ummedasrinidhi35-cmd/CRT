"""for i in range(1, 11):
    
    if i == 5:
        continue
    print(i,end=" ")
else:
    print("Loop completed")
   """
p1 = "Sri123"
for i in range(3):
    p2 = input()
    if p1 == p2:
        print("Login Successful")
        break
else:
    print("Account Locked")
