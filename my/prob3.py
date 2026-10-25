def longest_streak(minutes,threshold):
    sire = 0
    mz = []
    for i in range(len(minutes)):
        if minutes[i] >=threshold:
            sire+=1
        else:
            mz.append(sire)
            sire=0
    mz.append(sire)
    return(max(mz))

data = [70, 80, 10, 60, 65, 90]

print(longest_streak(data, 60))  # 3
print(longest_streak(data, 70))  # 2
print(longest_streak(data, 80))  # 1
