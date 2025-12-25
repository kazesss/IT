#1
def greet(name):
    return str("Добро пожаловать, " + name)
a = greet("Кира")
print(a)

#1.2
print("Введите число")
number = int(input())
def square(number):
    return number**2
print(square(number))

#1.3
print("Введите первое число")
x = int(input())
print("Введите второе число")
y = int(input())
def max_of_two(x, y):
    return max(x, y)
print(max_of_two(x, y))

#2
print("Введите свое имя")
name2 = str(input())
print("Введите свой возраст")
age = int(input())
def describe_person(name2, age=30):
    return (f"Name: {name2}, age: {age}")
print(describe_person(name2, age))

#3
print("Введите число")
num = int(input())
cnt = 0
def is_prime(num, cnt):
    for i in range(1, num + 1):
        if num % i == 0:
            cnt = cnt + 1
    if cnt == 2:
        return True
    else:
        return False
print(is_prime(num, cnt))