import random


def quick_sort(arr):
    if len(arr) < 2:
        return arr
    M = []
    L = []
    R = []
    for element in arr:
        if element == arr[0]:
            M.append(element)
        elif element < arr[0]:
            L.append(element)
        else:
            R.append(element)
    return quick_sort(L) + M + quick_sort(R)


# Задание 1
arr1 = [random.randint(-100, 100) for i in range(1000)]
print("До сортировки: ")
print(arr1)
print("После сортировки: ")
print(quick_sort(arr1))

# Задание 2
arr2 = [random.randint(50, 100) for i in range(10)]
print("До сортировки: ")
print(arr2)
print("После сортировки: ")
print(quick_sort(arr2))

# Задание 3
arr3 = [[random.randint(5, 61) for i in range(10)] for j in range(10)]
print("До сортировки: ")
print(arr3[0])
print("После сортировки: ")
print(quick_sort(arr3[0]))

# Задание 4
arr4 = []
for i in range(10):
    f = ""
    for j in range(random.randint(5, 10)):
        f += chr(random.randint(ord("А"), ord("Я")))
    arr4.append(f)

print("До сортировки: ")
print(arr4)
print("После сортировки: ")
print(quick_sort(arr4))
