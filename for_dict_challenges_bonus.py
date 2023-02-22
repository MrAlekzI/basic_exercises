"""
Пожалуйста, приступайте к этой задаче после того, как вы сделали и получили ревью ко всем остальным задачам
в этом репозитории. Она значительно сложнее.


Есть набор сообщений из чата в следующем формате:

```
messages = [
    {
        "id": "efadb781-9b04-4aad-9afe-e79faef8cffb",
        "sent_at": datetime.datetime(2022, 10, 11, 23, 11, 11, 721),
        "sent_by": 46,  # id пользователя-отправителя
        "reply_for": "7b22ae19-6c58-443e-b138-e22784878581",  # id сообщение, на которое это сообщение является ответом (может быть None)
        "seen_by": [26, 91, 71], # идентификаторы пользователей, которые видели это сообщение
        "text": "А когда ревью будет?",
    }
]
```

Так же есть функция `generate_chat_history`, которая вернёт список из большого количества таких сообщений.
Установите библиотеку lorem, чтобы она работала.

Нужно:
1. Вывести айди пользователя, который написал больше всех сообщений.
2. Вывести айди пользователя, на сообщения которого больше всего отвечали.
3. Вывести айди пользователей, сообщения которых видело больше всего уникальных пользователей.
4. Определить, когда в чате больше всего сообщений: утром (до 12 часов), днём (12-18 часов) или вечером (после 18 часов).
5. Вывести идентификаторы сообщений, который стали началом для самых длинных тредов (цепочек ответов).

Весь код стоит разбить на логические части с помощью функций.
"""
import random
import uuid
import datetime

#import lorem



def generate_chat_history():
    messages_amount = random.randint(200, 1000)
    users_ids = list(
        {random.randint(1, 10000) for _ in range(random.randint(5, 20))}
    )
    sent_at = datetime.datetime.now() - datetime.timedelta(days=100)
    messages = []
    for _ in range(messages_amount):
        sent_at += datetime.timedelta(minutes=random.randint(0, 240))
        messages.append({
            "id": uuid.uuid4(),
            "sent_at": sent_at,
            "sent_by": random.choice(users_ids),
            "reply_for": random.choice(
                [
                    None,
                    (
                        random.choice([m["id"] for m in messages])
                        if messages else None
                    ),
                ],
            ),
            "seen_by": random.sample(users_ids,
                                     random.randint(1, len(users_ids))),
            "text": 'some text' #lorem.sentence(),
        })
    return messages

def max_count(some_dict): #здесь функция чтобы делать список элементов с максимальными значениями(на случай если не один ключ с максимальным значением)
    users = []
    max_value = max(some_dict.values()) #ищем максимальное число сообщений
    for (key, value) in some_dict.items(): #ищем ключт у которых одинаковое и максимальное число
        if value == max_value:
            users.append(key)
    return " ".join(map(str, users))
     

def user_of_max (lst): #пользователь снаибольшим количеством сообщений
    users_dict = {} #создем словарь для подсчета
    for mesange in lst:
        users_dict[mesange['sent_by']] = users_dict.get(mesange['sent_by'], 0) + 1
    result = max_count(users_dict)
    return f'Пользователь(ли) написавшие наибольшее количество сообщений: {result}'


def max_reply(lst): #максимально цитируемые пользоатели
    reply_dict = {} 
    user_dict = {}
    for message in lst: #словарь реплаев
        if message['reply_for']:
            reply_dict[message['reply_for']] = reply_dict.get(message['reply_for'], 0) + 1
    for message  in lst: #еще раз проходимся по списку и сверяем id со ключами словаря реплаев
        if message['id'] in reply_dict: #если сообщение потом реплаится то пользователь отправившие его добавляется в словарь
            user_dict[message['sent_by']] = user_dict.get(message['sent_by'], 0) + reply_dict[message['id']]  #жобавляется количесвто реплаей конкретного сообщение пользовтаелся    
    result = max_count(user_dict)
    return f'Пользователь(ли) сообщения которого больше всего реплаили {result}'


def max_seen(lst): #максимально просматриваемые пользователи
    user_dict = {}
    for message in lst:
        user_dict[message['sent_by']] = user_dict.get(message['sent_by'], 0) + len(message['seen_by'])
    result = max_count(user_dict)
    return f'Наиболее просматриваемый пользователь(ли): {result}'
  

def max_time(lst):
    morning, day, evening = 0, 0, 0
    for message in lst:
            if message['sent_at'].hour < 12:
                morning += 1
            elif 12 <= message['sent_at'].hour <=18:
                day += 1
            else:
                evening += 1
    return f'Больше всего сообщений в чате {"утром" if morning>day and morning>evening else "днем" if day>morning and day>evening else "вечером"}'

count = 0
def max_tread (lst): #првоерка глубины треда c помощью рекурсии
    global count #счетчик глобальный чтобы не обнулялся при каждном входе в рекурсию, возможно можно проще
    reply_list = []
    for message in lst:
        if message['reply_for']:
            id = message['reply_for']
            reply_list.append(id)
    if len(reply_list) == 0:
        return f'Максимальная длина треда: {count}'
    else:
        count += 1
        new_lst = [message for message in lst if message['id'] in reply_list] #создаем который содержит родительские сообщения для реплаев на этом же шаге
        return max_tread(new_lst)


if __name__ == "__main__":
    message_list = generate_chat_history()
    print(user_of_max(message_list))
    print(max_reply(message_list))
    print(max_seen(message_list))
    print(max_time(message_list))
    print(max_tread(message_list))