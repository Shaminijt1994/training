n=[]
a=int(input("Enter the value of n:"))
for i in range (a):
    b=int(input("Enter the number:"))
def bubble_sort(b):
    for i in range(a):
         for j in range(n- 1):
            if n[j] > n[j+1]:
               n[j], n[j+1] = n[j+1], n[j]
bubble_sort(n)
print(n)
