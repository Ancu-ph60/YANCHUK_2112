first_element = int(input("Введіть перший елемент прогресії: "))
difference = int(input("Введіть різpyцю прогресії: "))

progression = [first_element + i * difference for i in range(10)]

print("Арифметична прогреія:", progression)
