sessions = [
    ("Telegram", 25),
    ("YouTube", 40),
    ("Telegram", 15),
    ("Browser", 30),
    ("YouTube", 20),
]
def summarize_sessions(sessions):
    res = {}
    for i in sessions:
        name, value = i

        if name in res:
            res[name]+=value
        else:
            res[name]=value
    return(res)

print(summarize_sessions(sessions))
print(summarize_sessions([]))

print(summarize_sessions([
    ("Browser", 10),
    ("Browser", 20),
    ("Browser", 5),
]))
