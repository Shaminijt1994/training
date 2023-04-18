from datetime import date
print("Enter the starting date:")
year_1= int(input('year1: '))
month_1 = int(input('month1: '))
day_1 = int(input('day1: '))
startdate = date(year_1,month_1,day_1)
print("Enter the ending date:")
year_2= int(input('year2: '))
month_2 = int(input('month2: '))
day_2= int(input('day2: '))
enddate = date(year_2,month_2,day_2)
d = enddate - startdate
print(d)



