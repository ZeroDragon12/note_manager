import greetings
import date_changer


def dictionary_print(dictionary):
    keys = dictionary.keys()
    for key in keys:
        if key.find('date') == -1:
            print(key, ':', dictionary[key])
        else:
            print(key, ':', date_changer.short_date(dictionary[key]))


choose = int(input('Готовые данные - 0, ручное заполнение -1: '))
if choose == 0:
    note = greetings.warp()
elif choose == 1:
    note = greetings.new_title()
else:
    note = None, None, None, None, None, None
title = {
    'username': note[0],
    'title': note[1],
    'content': note[2],
    'status': note[3],
    'crated_date': note[4],
    'issue_date': note[5],
}
dictionary_print(title)
