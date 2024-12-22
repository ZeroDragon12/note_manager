import add_input
import date_changer
import add_list

def new_title():
    username = 'username'
    title = 'title'
    content = 'content'
    status = 'not completed'
    created_date = '31-12-2024'
    issue_date = created_date
    print('Имя пользователя:', username)
    print('Заголовки:', title)
    print('Описание:', content)
    print('Статус:', status)
    print('Дата создания:', created_date)
    print('Дедлайн:', issue_date)
    username, title, content, status, created_date, issue_date = add_input.add_title(created_date)
    title = add_list.add_headers()
    print('Имя пользователя:',username)
    print('Заголовки:',title)
    print('Описание:',content)
    print('Статус:',status)
    print('Дата создания:',created_date)
    print('Дедлайн:',issue_date)
    date_changer.short_date_print(created_date)
    date_changer.short_date_print(issue_date)
    return username, title, content, status, created_date, issue_date