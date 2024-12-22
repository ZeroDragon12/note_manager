def add_title(date):
    username = input("Имя пользователя: ")
    title = input("Заголовок заметки: ")
    content = input("Описание заметки: ")
    status = input("Статус заметки: ")
    created_date = input(f"Дата создания в формате {date}: ")
    issue_date = input(f"Дата дедлайна в формате {date}: ")
    return username, title, content, status, created_date, issue_date
