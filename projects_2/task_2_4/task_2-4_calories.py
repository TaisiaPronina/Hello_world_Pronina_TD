protein_mass = float(input("Ввести массу белков (г): "))
fat_mass = float(input("ВВести массу жиров (г): "))
carbohydrates_mass = float(input("Ввести массу углеводов (г): "))


callories = (protein_mass * 4) + (fat_mass * 9) + (carbohydrates_mass * 4)


print(f"Количество калорий: {callories} ккал")