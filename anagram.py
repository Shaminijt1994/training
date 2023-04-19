s1=input("Enter the first word:")
s2=input("Enter the second word:")
if(len(s1)==len(s2)):
    sorted_s1 = sorted(s1)
    sorted_s2 = sorted(s2)
    if(sorted_s1==sorted_s2):
        print("They are balanced.")
    else:
        print("They are not balanced.")