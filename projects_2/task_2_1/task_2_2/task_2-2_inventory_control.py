reagent_name = input("Введите название реактива: ")
amount_of_reagent = int(input("Введите количество реактива: "))

print (f"Реактив {reagent_name} в количестве {amount_of_reagent} шт поступил на склад")

with open("inventory.txt", "w", encoding="utf-8") as file:
    file.write(f"Реактив [{reagent_name}] поступил на склад в количестве [{amount_of_reagent}] шт.")