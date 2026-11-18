with open("study_note.txt", "w", encoding="utf-8") as file:
    file.write("Изучаю файлы\n Сегодня записал и прочитал текст")
file.close()

with open("study_note.txt", "r", encoding="utf-8") as file:
    text = file.read()
print(text)