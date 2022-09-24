def convtuple(tu, st):
    sus = []
    for i in tu:
        sus.append(i)
        sus.append(st)

    return tuple(sus)

tup = input('enter number seperated by space')
li = (int(x) for x in tup.split(' '))
k = input('Enter a string random ')
print(convtuple(li,k))
