n=[]
a=int(input("Enter the value of n:"))
for i in range (a):
    b=int(input("Enter the number:"))
    n.append(b)
print("The largest number in the list is:",max(n),"\n The smallest number in the list is",min(n))
sum = 0
for i in range (a):
    sum = sum + n[i]
    average = sum/a
print("The average of the numbers in the list is:",average)
x = average
closestvalue=n[0]
dis=abs(x-closestvalue)
for i in range (0,x):
    if(abs(x-closestvalue < dis)):
        closestvalue = n[i]
        dis=abs(x-closestvalue)
    print("The closest value of the average is:")