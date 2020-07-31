print("Задание 1")

my_list = [11, "Hi", [1, 2], 2.878]


def my_type(el):
    for el in range(len(my_list)):
        print(type(my_list[el]))
    return


my_type(my_list)

print("\nЗадание 2")

el_count = int(input("Введите количество элементов списка "))
my_list = []
i = 0
el = 0
while i < el_count:
    my_list.append(input("Введите следующее значение списка "))
    i += 1

for elem in range(int(len(my_list) / 2)):
    my_list[el], my_list[el + 1] = my_list[el + 1], my_list[el]
    el += 2
print(my_list)

print("\nЗадание 3")

seasons_list = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь',
                'Декабрь']
seasons_dict = {1: 'Зима', 2: 'Весна', 3: 'Лето', 4: 'Осень'}
month = int(input("Введите месяц по номеру "))
if month == 1 or month == 12 or month == 2:
    print(seasons_dict.get(1))
if month == 1:
    print(seasons_list[0])
if month == 2:
    print(seasons_list[2])
if month == 12:
    print(seasons_list[13])
elif month == 3 or month == 4 or month == 5:
    print(seasons_dict.get(2))
    if month == 3:
        print(seasons_list[2])
    if month == 4:
        print(seasons_list[3])
    if month == 5:
        print(seasons_list[4])

elif month == 6 or month == 7 or month == 8:
    print(seasons_dict.get(3))
    if month == 6:
        print(seasons_list[5])
    if month == 7:
        print(seasons_list[6])
    if month == 8:
        print(seasons_list[7])

elif month == 9 or month == 10 or month == 11:
    print(seasons_dict.get(4))
    if month == 9:
        print(seasons_list[8])
    if month == 10:
        print(seasons_list[9])
    if month == 11:
        print(seasons_list[10])

else:
    print("Такого месяца не существует")

print("\nЗадание 4")

my_str = input("введите строку из нескольких слов")
my_word = []
num = 1
for el in range(my_str.count(' ') + 1):
    my_word = my_str.split()
    if len(str(my_word)) <= 10:
        print(f" {num} {my_word[el]}")
        num += 1
    else:
        print(f" {num} {my_word[el][0:10]}")
        num += 1

print("\nЗадание 5")

my_list = [6, 4, 3, 2, 2]
print(f"Рейтинг - {my_list}")
digit = int(input("Введите новый элемент рейтинга "))
while digit != 100:
    for el in range(len(my_list)):
        if my_list[el] == digit:
            my_list.insert(el + 1, digit)
            break
        elif my_list[0] < digit:
            my_list.insert(0, digit)
        elif my_list[-1] > digit:
            my_list.append(digit)
        elif my_list[el] > digit and my_list[el + 1] < digit:
            my_list.insert(el + 1, digit)
    print(f"текущий список - {my_list}")
    digit = int(input("Введите число "))

print("\nЗадание 6")

goods = []
features = {'name': '', 'price': '', 'quantity': '', 'unit': ''}
analytics = {'name': [], 'price': [], 'quantity': [], 'unit': []}
num = 0
feature_ = None
control = None
while True:
    control = input("For quit press 'Q', for continue press 'Enter', for analytics press 'A'").upper()
    if control == 'Q':
        break
    num += 1
    if control == 'A':
        print(f'\n Current analytics \n {"-" * 30}')
        for key, value in analytics.items():
            print(f'{key[:25]:>30}: {value}')
            print("-" * 30)
    for f in features.keys():
        feature_ = input(f'Input feature "{f}"')
        features[f] = int(feature_) if (f == 'price' or f == 'quantity') else feature_
        analytics[f].append(features[f])
    goods.append((num, features))
