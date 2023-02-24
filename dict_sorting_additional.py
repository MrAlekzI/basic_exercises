'''
Дополнительное задание:
Посчитать число буквв слове и вывести начиная с самой часто встречающейся и дльше по убыванию.
 Если несколько букв встречаются в слове одинаковое число раз,
 то вывести вперед ту что раньше в алфавите. Написать три решения - использую просто словарь, defaultdict и Counter.
'''
from collections import defaultdict, Counter
import string
import random

def letter_counter_dict(word): #решение 1 через словарь
    #word_list = sorted(list(word)) #переводим в стисок и сортируем чтобы при одинкаовых количесвах буквы бли в алфавитном порядке
    letter_dict = {}
    for letter in word: #формируем словарь через get
        letter_dict[letter] = letter_dict.get(letter, 0) + 1
   
    result1 = sorted(letter_dict.items(), key=lambda item: item[0]) #сортировка по алфафиту после подсчета
    result2 = sorted(result1, key=lambda item: item[1], reverse=True) #обратная сортировка по значению
    for (key, value) in result2:
        print(key, value, end=' ')

def letter_counter_dict_2(word): #решение 2 через defaultdict
    #word_list = sorted(list(word))
    letter_dict = defaultdict(lambda: 0) #задаем дефолное значения ключа
    for letter in word: #формируем словарь
        letter_dict[letter] += 1

    result1 = sorted(letter_dict.items(), key=lambda item: item[0]) #сортировка по алфафиту после подсчета
    result2 = sorted(result1, key=lambda item: item[1], reverse=True) #обратная сортировка по значению
    for (key, value) in result2:
        print(key, value, end=' ')

def letter_counter_dict_3(word): #решение 3 через Counter
    word_list = sorted(list(word))
    letter_dict = Counter(word_list) 
    result = letter_dict.most_common()
    for (key, value) in result:
        print(key, value, end=' ')
 

if __name__ == '__main__':

    random_string = 'pnbalkpanactlnca'
    #test_string = ''.join(random.choices(string.ascii_letters, k=100000))
    print('Способ 1')
    letter_counter_dict(random_string)
    print ('\nСпособ 2')
    letter_counter_dict_2(random_string)
    print ('\nСпособ 3')
    letter_counter_dict_3(random_string)