'''1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
'''

months =  [("January",31),["February", 28],("March",31),
                       ("April", 30), ("May", 31), ("June", 30),
                       ("July", 31), ("August", 31), ("September", 30),
                       ("October", 31), ("November", 30), ("December", 31)]

def daysInYear(year):
    if year%4 ==0 and year %100 != 0 or year%400 ==0:
        return 366
    else:
        return 365
_1Junuary1900 = 1                                #1 it's monday,7 - it's sunday, divide to 7 by module
_1Junuary1901 = daysInYear(1900)%7 + _1Junuary1900
firstSundays = 0
myday = _1Junuary1901

for i in range(1901,2001):
    if daysInYear(i) == 366:
        months[1][1] = 29
    else:
        months[1][1] = 28
    for month in months:
        myday = myday%7 + (month[1])%7


        if (myday)%7 == 0:
            firstSundays+=1
        print(firstSundays)
        print(myday)
print(firstSundays)
