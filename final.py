note = {}

note["username"] =input("Введите имя пользователя:")
title1 = input("Введите заголовок заметки 1: ")
title2 = input("Введите заголовок заметки 2: ")
title3 = input("Введите заголовок заметки 3: ")
titles = [
    title1, title2, title3
]
note["titles"]=titles
note["content"] =input("Введите описание заметки:")
note["status"] =input("Введите статус заметки:")
note["created_date"] =input("Введите дату создания в формате ДД.ММ.ГГГГ:")
note["issue_date"] =input("Введите дату окончания в формате ДД.ММ.ГГГГ:")

print("\nСобранная информация:")
print("Имя пользователя:", note["username"])
print("Заметки:", note["titles"])
print("Описание заметки:", note["content"])
print("Статус:", note["status"])
print("Дата создания:", note["created_date"])
print("Дата окончания:", note["issue_date"])