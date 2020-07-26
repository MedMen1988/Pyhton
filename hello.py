print("Задание 1")
name = input("Привет, как твоё имя? ")
age = int(input("Сколько тебе лет? "))

print(f"Привет {name}!")

print("\nЗадание 2")
a = int(input("Введите время в секундах "))
h = a//3600
m = (a//60)%60
s = a%60
print( "Ваше время "'%02d:%02d:%02d'% (h, m, s) )

print("\nЗадание 3")
a = int(input("Найдите сумму чисел n + nn + nnn. Введите число "))
b = str(a)
b1 = b + b
b2 = b + b + b
c = a + int(b1) + int(b2)

print(f"Результат {c}")