sessions = [
    ("Telegram", 25),
    ("YouTube", 40),
    ("Telegram", 15),
    ("Browser", 30),
    ("YouTube", 20),
]

while True:
    title = input("Введите сервис: ")
    title = title.strip()
    if title.lower() == "стоп":
        break
    if len(title) == 0:
        print("Название не может быть пустым")
        continue
    else:
        try:
            ttime = int(input("сколько минут "))
            if ttime < 0:
                print("время не может быть отрицательным")
                continue
            sessions.append((title,ttime))
        except ValueError:
            print("введите числом")

def summarize_sessions(sessions):
    res = {}
    for i in sessions:
        name, value = i
        if name in res:
            res[name]+=value
        else:
            res[name]=value
    return(res)

totals = summarize_sessions(sessions)
t =0
for name in totals:
    print(name,":",totals[name] , "мин")
    t +=totals[name]
print("Всего:", t,"мин")