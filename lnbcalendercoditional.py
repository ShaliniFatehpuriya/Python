def check(date):
    #print(date)
    month = date[1]
    if 1<month<=4:
        print('season : Spring')
    elif 4<month<=7:
        print('season : Summer')
    else:
        print('season : Winter')

    if (date[2]%4==0) and (date[2]%100 !=0) or (date[2]%400==0):
        print(f'No. of days are 366')
    else:
        year = date[2]
        con = True
        while con :
            year+=1
            if (year%4==0) and (year%100 !=0) or (year%400==0):
                print(f'Next leap year is {year}')
                con = False
            
ip = input("Enter a date as dd mm yyyy ").split()
date=[]
for i in ip:
    date.append(int(i))
print(check(date))
