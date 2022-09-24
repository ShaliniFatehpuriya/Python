l1 = []
l2 = []
em_d = {}
for i in range(3):
    key = input('enter the key')
    if key not in l1:
        l1.append(key)


for i in range(3):
    value = input('enter a value')
    if value not in l2:
        l2.append(value)

for i in range(len(l1)):
    em_d[l1[i]]=l2[i]

print(em_d)
