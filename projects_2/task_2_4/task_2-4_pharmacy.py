capsules_produced = int(input("Ввведите общее количество произведённых капсул: "))
in_one_package = int(input("Веедите количество капсул в одной упаковке: "))
 
print(f"Введите общее количество произведённых капсул: {capsules_produced}")
print(f"ВВедите количество капсул в одной упаковке: {in_one_package}")

full_packages = capsules_produced // in_one_package
remaining_capsules = capsules_produced % in_one_package


print("\n---Отчет фасовочного цеха---")
print(f"Полных упаковок: {full_packages}")
print(f"Остаток капсул: {remaining_capsules}")