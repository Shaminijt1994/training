n = int(input("Enter the number: "))
c = 1
for j in range(2,(n//2 + 1)):
    if(n % j == 0):
        c = 0
        break

if(c==1):
    print("This is a prime number")
else:
    print("This is not a prime number")
