while True:
    title = input("Введите сервис: ")
    if title == "." or len(title) == 0:
        break
    print(len(title))