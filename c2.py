# numbers = input("Enter numbers: ").split()
# numbers = [int(num) for num in numbers]
# count = 0
# for i in range(1, len(numbers)):
#     if numbers[i] > numbers[i-1]:
#         count += 1
# print(f"Number of elements, greater than the previous one: {count}")

# numbers1 = input("Enter numbers: ").split()
# numbers1 = [int(num) for num in numbers1]
# count = {}
# for num in numbers1:
#     if num in count:
#         count[num] += 1
#     else:
#         count[num] = 1
# unique = [num for num in numbers1 if count[num] == 1]
# print(f"Elements that appear only once: {unique}")

# numbers2 = input("Enter numbers: ").split()
# numbers2 = [int(num) for num in numbers2]
# max = 1
# curr = 1
# max1 = [numbers2[0]]
# curr1 = [numbers2[0]]
# for i in range(1, len(numbers2)):
#     if numbers2[i] > numbers2[i-1]:
#         curr += 1
#         curr1.append(numbers2[i])
#     else:
#         if curr > max:
#             max = curr
#             max1 = curr1.copy()
#         curr = 1
#         curr1 = [numbers2[i]]
# if curr > max:
#     max = curr
#     max1 = curr1.copy()
# print(f"Length: {max}")
# print(f"Sequence: {max1}")

# numbers4 = input("Enter numbers: ").split()
# numbers4 = [int(num) for num in numbers4]
# N = int(input("Enter the number of positions to shift right: "))
# N = N % len(numbers4)
# shift = numbers4[-N:] + numbers4[:-N]
# print(f"Original list: {numbers4}")
# print(f"Shifted list: {shift}")

import random
list11 = [random.randint(1, 20) for _ in range(10)]
list2 = [random.randint(1, 20) for _ in range(10)]
combined = list11 + list2
uniquec = list(set(combined))
common = list(set(list11) & set(list2))
unique1 = list(set(list11) - set(list2))
unique2 = list(set(list2) - set(list11))
uniquee3 = unique1 + unique2
min_max = [min(list11), max(list11), min(list2), max(list2)]
while True:
    print("Оберіть варіант списку для виведення:")
    print("1. Початкові списки")
    print("2. Об'єднаний список")
    print("3. Об'єднаний список без повторень")
    print("4. Спільні елементи")
    print("5. Унікальні елементи кожного списку")
    print("6. Мінімальні та максимальні значення")
    print("0. Вийти")
    choice = input("Ваш вибір (0-6): ")
    
    if choice == '1':
        print(f"Перший список: {list11}")
        print(f"Другий список: {list2}")
    elif choice == '2':
        print(f"Об'єднаний список: {combined}")
    elif choice == '3':
        print(f"Об'єднаний список без повторень: {uniquec}")
    elif choice == '4':
        print(f"Спільні елементи: {common}")
    elif choice == '5':
        print(f"Унікальні елементи: {uniquee3}")
    elif choice == '6':
        print(f"Мінімальні та максимальні значення: {min_max}")
    elif choice == '0':
        print("Дякуємо за використання програми!")
        i = False
        break
    else:
        print("Помилка! Будь ласка, оберіть число від 0 до 6.")