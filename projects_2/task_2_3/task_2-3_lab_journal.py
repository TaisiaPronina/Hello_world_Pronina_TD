resercher_name = input("Введите ФИО исследователя: ")
experiment_date = input("Введите дату: ")
experiment_name = input("Введите название эксперимента: ")
experiment_result = input("Введите вывод: ")


with open("journal.txt", "w", encoding="utf-8") as file:
    file.write("Электронный лабораторный журнал\n", end="|_______________________________________________________|\n")
    file.write(f"ФИО исследователя:\t{resercher_name}\nДата:\t{experiment_date}\nНазвание эксперимента:\t{experiment_name}\n", end="|_______________________________________________________|\n")
    file.write(f"Вывод:\n{experiment_result}\n", end="|_______________________________________________________|\n")
    
print("Данные успешно сохранены в journal.txt")

