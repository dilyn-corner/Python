def leapYear(year):
    if year%100==0 and year%400!=0:
        print('false') 
    elif year%4==0:
        print('true')
    else:
        print('false')
