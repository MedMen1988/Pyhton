print("Задание 1")
name = input("Привет, как твоё имя? ")
age = int(input("Сколько тебе лет? "))

print(f"Привет {name}!")

print("\nЗадание 2")
a = int(input("Введите время в секундах "))
h = a//3600
m = (a//60)%60
s = a%60
if h<10:
    h=str('0'+str(h))
else:
    h=str(h)
if m<10:
    m=str('0'+str(m))
else:
    m=str(m)
if s<10:
    s=str('0'+str(s))
else:
    s=str(s)
print(f"Ваше время {str(h)}:{str(m)}:{str(s)}")

