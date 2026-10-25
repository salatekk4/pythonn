sessions = [
    ("Telegram", 25),
    ("YouTube", 40),
    ("Telegram", 15),
    ("Browser", 30),
    ("YouTube", 20),
]
# res = []
# for i in sessions:
#     n,v = i
#     q = 0
#     for _ in sessions:
#         n1,v1= _
#         if n1 == n:
#             q += v1
#     res.append((n,q))
# print(res)

# res = {}
# for i in sessions:
#     name, value = i
#     q = 0
#     for _ in sessions:
#         name1, value1 = _
#         if name1 == name:
#             q+= value1
#     res[name] = q

# print(res)

res = {}
for i in sessions:
    name, value = i
    q = 0
    if name in res:
        res[name]+=value
    else:
        res[name]=value
print(res)