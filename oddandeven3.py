a = input("Enter the word:")
oddplaces=[]
evenplaces=[]
evenplace=0
oddplace=1
for i in range (len(a)):
    if(i%2==0):
        evenplaces = evenplaces + [a[i]]
    else:
        oddplaces = oddplaces + [a[i]]
print("The even places of the string is",evenplaces)
print("The odd places of the string is",oddplaces)
    