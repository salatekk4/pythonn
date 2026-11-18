minutes = [70, 80, 10, 60, 65, 90]
sire = 0
mz = []
for i in range(len(minutes)):
    if minutes[i] >=60:
        sire+=1
    else:
        mz.append(sire)
        sire=0
mz.append(sire)
print(max(mz))