weight = float(input("Введите вес (кг): "))
height = float(input("Введите рост (м): "))

print(f"Введите ваш вес (кг): {weight}")
print(f"Введите ваш рост (м): {height}\n")

bmi = weight / (height ** 2)

print("---Отчет о состоянии здоровья---")
print(f"Рост:\t{height}\nВес:\t{weight}\nИндекс массы тела:\t{bmi}")