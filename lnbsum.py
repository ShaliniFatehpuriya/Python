def sum_five_integer():
    lst=[]
    sm = 0
    for i in range(5):
        a = int(input('enter 5 digits'))
        if a>9:
            lst.append(a)
            sm+=a
    return sm

print(sum_five_integer())
