import greetings
def dictionary_print(dictionary):
    keys = dictionary.keys()
    for key in keys:
        print(key,':', dictionary[key])

note = greetings.new_title()
title = {
    'username': note[0],
    'title': note[1],
    'content': note[2],
    'status': note[3],
    'crated_date': note[4],
    'issue_date': note[5],
}
dictionary_print(title)
