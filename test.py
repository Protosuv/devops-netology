# тестовая шуточная программа
age = int(input("Сколько тебе лет? "))
print(age)
if age >= 0 and age <= 10:
    print("Ты маленький")
elif age >= 11 and age <= 20:
    print("Ты тинейджер")
elif age >= 21 and age <= 30:
    print("Ты молодой")
elif age > 30 and age <= 50:
    print("Ты среднего возраста")
elif age > 50 and age <= 70:
    print("Ты пожилой")
elif age > 70 and age < 91:
    print("Ты старенький")
else:
    print("Ты суперстар")