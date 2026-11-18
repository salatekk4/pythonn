expenses = [
    ("Еда", 350),
    ("Транспорт", 60),
    ("Еда", 200),
    ("Учёба", 450),
    ("Транспорт", 90),
]

expenses1 = [

]
expenses2 = [
    ("Еда", 350),
    ("Еда", 123)
]
def summarize_expenses(records):
    res ={}
    for i in records:
        name, value = i
        if name in res:
            res[name] +=value
        else:
            res[name] = value
    return res

print(summarize_expenses(expenses))
print(summarize_expenses(expenses1))
print(summarize_expenses(expenses2))