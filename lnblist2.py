l1 = list(range(1,20))
new_list = l1[:5] 
for i in l1[-6:]:
    new_list.append(i)
    l2 = []
for i in new_list:
    l2.append(int(i)**2)
test = l2[:2]
final = []
final.append(test)
final.append(l2[2:5])
final.append(l2[5:])
print(final)
