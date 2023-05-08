# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества. 
# Затем пользователь вводит сами элементы множеств.

# n = int(input('Print a length of first set: '))
# m = int(input('Print a length of second set: '))

# list_n = []
# list_m = []

# for i in range(n):
#     list_n.append(int(input('Print an element for first set: ')))

# for i in range(m):
#     list_m.append(int(input('Print an element for second set: ')))

# print(list_n)
# print(list_m)

# list_3 = []

# for item in list_n:
#     if item in list_m:
#         list_3.append(item)

# list_3 = set(list_3)
# max = 0
# temp = 0

# for item in list_3:
#     if item > max:
#         temp = max
#         max = item
#         item = temp


# print(list_3)



# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. 
# Она растёт на круглой грядке, причём кусты высажены только по окружности. 
# Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растёт N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло 
# различное число ягод — на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники. 
# Эта система состоит из управляющего модуля и нескольких собирающих модулей. 
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, 
# собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, 
# которое может собрать за один заход собирающий модуль, 
# находясь перед некоторым кустом заданной во входном файле грядки.


n = int(input('Print a sum of bushes: '))
berries = []

for i in range(n):
    berries.append(int(input('Print a sum of berries on current bush: ')))


list_sums = []
for i in range(len(berries)):
    if i == 0:
        list_sums.append(berries[i] + berries[len(berries)-1] + berries[i+1])
    elif i == len(berries):
        list_sums.append(berries[i] + berries[i-1] + berries[0])
    elif i > 0 and i < (len(berries) - 1):
        list_sums.append(berries[i] + berries[i-1] + berries[i+1])
    i += 1

max = 0
for item in list_sums:
    if item > max:
        max = item
print(max)