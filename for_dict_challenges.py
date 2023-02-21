# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика
# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2

students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Петя'},
]
first_name_dict = {}
for person in students:
    if person['first_name'] in first_name_dict:
       first_name_dict[person['first_name']] +=1
    else:
       first_name_dict[person['first_name']] = 1 
    
for k,v in first_name_dict.items():
       print(f'{k}: {v}')

# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя
# Пример вывода:
# Самое частое имя среди учеников: Маша
students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
]

def name_counter(students):
    name_dict = {}
    for person in students:
        if person['first_name'] in name_dict:
            name_dict[person['first_name']] +=1
        else:
            name_dict[person['first_name']] = 1
    maximal = max(name_dict.values()) #чтобы не связываться с сортирокой словаря
    for (k, v) in name_dict.items():
        if v == maximal:
            print(k, end=' ') #печать а не return на случай если несколько имен с одинаковой встерчаемостьб, и чтобы не формирововать лишний раз список
    print('\n') #возвращаем каретку в начало
print('Самое чаcтое имя: ', end='')
name_counter(students) 

# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша

school_students = [
    [  # это – первый класс
        {'first_name': 'Вася'},
        {'first_name': 'Вася'},
    ],
    [  # это – второй класс
        {'first_name': 'Маша'},
        {'first_name': 'Маша'},
        {'first_name': 'Оля'},
    ],[  # это – третий класс
        {'first_name': 'Женя'},
        {'first_name': 'Петя'},
        {'first_name': 'Женя'},
        {'first_name': 'Саша'},
    ],
]
for i in range(len(school_students)):
    print (f'Самое распространненое имя в классе {i+1}: ', end='' )
    name_counter(school_students[i]) #использовал функцию из задачи 2



# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
# Пример вывода:
# Класс 2a: девочки 2, мальчики 0 
# Класс 2б: девочки 0, мальчики 2

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '2б', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
    {'class': '2б', 'students': [{'first_name': 'Даша'}, {'first_name': 'Олег'}, {'first_name': 'Маша'}]},
]
is_male = {
    'Олег': True,
    'Маша': False,
    'Оля': False,
    'Миша': True,
    'Даша': False,
}

def gender_count(pupil):
    m, f = 0, 0
    for person in pupil:
        if is_male.get(person['first_name']):
            m+=1
        else:
            f+=1
    return (m,f) #здесь пробую кортеж чтобы не делать дополнительный словарь каждый раз

for clas in school:
    print(f'Класс {clas["class"]}: девочки {gender_count(clas["students"])[1]}, мальчики {gender_count(clas["students"])[0]}')


# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков
# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
    'Маша': False,
    'Оля': False,
    'Олег': True,
    'Миша': True,
}

count_dict = {}
for clas in school:
    count_dict[clas['class']] = gender_count(clas["students"])
#здесь пожалуй воспользуюсь сортировкой
boys = sorted(count_dict.items(), key=lambda item: item[1][0])[-1][0]
girls = sorted(count_dict.items(), key=lambda item: item[1][1])[-1][0]
print(f'Больше всего мальчиков в классе {boys} \nБольше всего девочек в классе {girls}')


