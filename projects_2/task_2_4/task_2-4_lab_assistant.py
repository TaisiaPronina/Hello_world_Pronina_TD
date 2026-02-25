solution_volume = int(input("Введите необходмый объём раствора (мл): "))
salt_mass = solution_volume * 0.009
water_volume  = solution_volume

with open("recipe.txt", "w", encoding="utf-8") as file:

    file.write(f"ОТЧЕТ ПО ПРИГОТОВЛЕНИЮ\n - * 23\n Общий объём: {solution_volume} мл\n Масса сооли: {salt_mass:.2f} г\n Объём воды: {water_volume} мл\n")
repeat = "-" * 23

print(f"ОТЧЕТ ПО ПРИГОТОВЛЕНИЮ\n {repeat}\n Общий объём: {solution_volume} мл\n Масса сооли: {salt_mass:.2f} г\n Объём воды: {water_volume} мл\n")
print("Рецепет сохранен в  файл")