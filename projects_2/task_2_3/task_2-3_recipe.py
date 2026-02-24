nutrient_medium = input("Введите название питательной среды: ")
agar_concentration = input("Введите концентрацию агара (%): ")
sterilixation_temperature = input("Введите температуру стерилизации(°С): ")

print(f"Название питательной среды: {nutrient_medium}\nКонцентрация агара: {agar_concentration}%\nТемпература стерилизации: {sterilixation_temperature}°С")

with open("recipe.txt", "w", encoding="utf-8") as file:
    file.write(f"{nutrient_medium}\n")
    file.write(f"Концентрация агара: {agar_concentration}%\n")
    file.write(f"Температура стерилизации: {sterilixation_temperature}°C\n")


    print("\nФайл 'recipe.txt' успешно сформирован!")