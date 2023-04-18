n=int(input("Enter the number of elements:"))
n_1 = 0
n_2 = 1
count = 0
if(n<0):
    print("Valid only for positive integers.")
elif (n==1):
    print("The fibonacci sequence upto",n,":")
    print (n_1)
else:
    print("The fibonacci sequence is:")
    while(count<n):
        print(n_1)
        a = n_1+n_2
        n_1 = n_2
        n_2 = a
        count = count +1
