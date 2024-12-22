import add_input
import date_changer
import add_list


def warp():
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
    print('Краткая дата создания:', date_changer.short_date(created_date))
    print('Краткая дата дедлайна:', date_changer.short_date(issue_date))


def new_title():
    username, title, content, status, created_date, issue_date = add_input.add_title('31-12-2024')
    title = add_list.add_headers()
    print('Имя пользователя:', username)
    print('Заголовки:', title)
    print('Описание:', content)
    print('Статус:', status)
    print('Дата создания:', created_date)
    print('Дедлайн:', issue_date)
    print(date_changer.short_date(created_date))
    print(date_changer.short_date(issue_date))
    return username, title, content, status, created_date, issue_date
