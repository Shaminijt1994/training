def check_if_list_has_value(list, value):
    try:
        if list.index(value) >= 0:
            return True
    except:
        pass
    return False

def union(s1, s2):
    s3 = []
    s3 = s3 + s1
    for i in range(len(s2)):
        if check_if_list_has_value(s3, s2[i]) ==  False:
            s3.append(s2[i])
    return s3

def intersect(s1, s2):
    s3 = []
    choice = "s1"
    if len(s1) <= len(s2):
        choice = "s2"
    if choice == "s1":
        size = len(s1)
        for i in range(size):
            if check_if_list_has_value(s2, s1[i]) == True:
                s3.append(s1[i])
    else:
        size = len(s2)
        for i in range(size):
            if check_if_list_has_value(s1, s2[i]) == True:
                s3.append(s2[i])
    return s3

def subtract(s1, s2):
    s3 = []
    for i in range(len(s1)):
        if check_if_list_has_value(s2, s1[i]) == False:
            s3.append(s1[i])
    return s3

s_1=[]
n_1= int(input("Enter the number of values in set s_1:"))
for i in range (n_1):
    b = input("Enter the a value for set 1:")
    if check_if_list_has_value(s_1, b) == False:
        s_1.append(b)

s_2=[]
n_2= int(input("Enter the number of values in set s_2:"))
for i in range (n_2):
    b = input("Enter the a value for set 2:")
    if check_if_list_has_value(s_2, b) == False:
        s_2.append(b)

print("S1 is:")
print(s_1)
print("S2 is:")
print(s_2)

print("Union of S1 and S2 is:")
print(union(s_1, s_2))

print("Intersection of S1 and S2 is:")
print(intersect(s_1, s_2))

print("Difference of S1 and S2 is:")
print(subtract(s_1, s_2))