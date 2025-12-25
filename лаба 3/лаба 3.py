#1 задание
x = input('Введите тип чтения(полностью или по строкам): ')

if x == 'полностью':
    with open('/лабы ит/example.txt', 'r') as file:
         content = file.read()
         print(content)
elif x == 'по строкам':
     with open('/лабы ит/example.txt', 'r') as file:
        for line in file:
            print(line)

#2 задание
text = input('Введите текст: ')
y = input('Введите действие(создать или добавить): ')

if y == 'создать':
    with open('/лабы ит/user_input.txt', 'w') as file:
        file.write(text)
elif y == 'добавить':
    with open('/лабы ит/user_input.txt', 'a') as file:
        file.write(text)

#3 задание
z = str(input('Введите тип чтения(полностью или по строкам): '))

try:
    if z == 'полностью':
        with open('/Users/kira/PycharmProjects/pythonProject1/example.txt', 'r') as file:
             content = file.read()
             print(content)
    elif z == 'по строкам':
         with open('/Users/kira/PycharmProjects/pythonProject1/example.txt', 'r') as file:
             for line in file:
                 print(line)
except FileNotFoundError:
    print('Error')