#Домашняя работа по уроку "Пространство имён"

calls = 0

def count_calls():
    global calls
    calls += 1

def string_info(string):
    count_calls()
    kort = [len(string), string.lower(), string.upper()]
    return kort

def is_contains(str, kort):
    count_calls()
    for string in kort:
        if str.lower() == string.lower():
            return True
    return False


string = "KrutoBoss"

print(string_info(string))

str = "Urban"
kort = ['ban', 'BaNaN', 'urBAN']

print(is_contains(str, kort))

print(calls)