def add_headers():
    first_header = input("Введите первый заголовок: ")
    second_header = input("Введите второй заголовок: ")
    third_header = input("Введите третий заголовок: ")
    print("Первый заголовок: ", first_header)
    print("Второй заголовк: ", second_header)
    print("Третий заголовок: ", third_header)
    headers = [first_header, second_header, third_header]
    print(headers)
    return headers
