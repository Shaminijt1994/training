import math

def find_area(*sides):
    if len(sides)==1:
        return sides[0]*sides[0]
    elif len(sides)==2:
        return sides[0]*sides[1]
    elif len(sides)==3:
        s = (sides[0] + sides[1] + sides[2])/2
        area = math.sqrt( s * (s-sides[0]) * (s-sides[1]) * (s-sides[2]))  
        return area  
    else:
        return False
    
print(find_area(13))
print(find_area(21, 47))
print(find_area(10, 20, 12))