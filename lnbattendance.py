def max_streak(wor, days, data):
    streak = []
    stk=1
    i=0
    counter = True
    for day in data:
        if day =='P'*wor:
            streak.append(1)
        else:
            streak.append(0)

    for i in range(days-1):
        if streak[i] == 1 and streak[i+1] ==1:
            stk+=1
    return stk
    
e = 5
w = 7
each_data = ['PPPPP','PPPPP','PPPPP', 'AAAPP', 'PAPAP', 'AAAAA', 'PAAAP']
print(max_streak(e,w,each_data))
