def max_streak(wor, days, data):
    streak = []
    count = 0
    result = 0
    for day in data:
        if day =='P'*wor:
            streak.append(1)
        else:
            streak.append(0)

    for i in range(0,days):

        if (streak[i] == 0):
            count = 0
        else:
            count+= 1
            result = max(result, count)         
    return result

e = 5
w = 7
each_data = ['PPPPP','PPPPP', 'AAAPP', 'PAPAP','AAAAA','PPPPP', 'PAAAP']
print(max_streak(e,w,each_data))
