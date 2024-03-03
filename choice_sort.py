import random


def choice_sort_1(arr):
    n = len(arr)
    for i in range(n - 1):
        min_ind = i
        for j in range(i + 1, n):
            if arr[min_ind] > arr[j]:
                arr[min_ind], arr[j] = arr[j], arr[min_ind]


def choice_sort_2(arr):
    n = len(arr)
    for i in range(n - 1):
        min_ind = i
        for j in range(i + 1, n):
            if arr[min_ind] < arr[j]:
                arr[min_ind], arr[j] = arr[j], arr[min_ind]


n = 10

# Задание 1
arr1 = []
for i in range(n):
    arr1.append(random.randint(2, 103))
print("До сортировки:")
print(arr1)
choice_sort_1(arr1)
print("После сортировки:")
print(arr1)

# Задание 2
arr2 = []
for i in range(n):
    arr2.append(random.randint(0, 100))
print("До сортировки:")
print(arr2)
choice_sort_2(arr2)
print("После сортировки:")
print(arr2)

# Задание 3
arr3 = []
for i in range(n):
    arr3.append(str(random.randint(10, 99)) + "-" + str(random.randint(10, 99)) + "-" + str(random.randint(10, 99)))
print("До сортировки:")
print(arr3)
choice_sort_1(arr3)
print("После сортировки:")
print(arr3)
