#program to find leap year or not

year=int(input("Enter the year to check :"))

#divide by 100 menas century year (ending with 00)
#century year divided by 400 is leap year

if (year % 400 ==0) and (year % 100 ==0):
    print("{0} is a leap year ".format(year))

# not divided by 100 means not a century year
elif (year % 4==0) and (year % 100!=0):
    print("{0} is a leap year".format(year))

#if not divided by both 400 (century year) and 4
else:
    print("{0} is not a leap year ".format(year))
