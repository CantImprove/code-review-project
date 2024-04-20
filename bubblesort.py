def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # Установка флага, который будет указывать, были ли сделаны обмены на этой итерации
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        # Если на данной итерации не было сделано ни одного обмена, массив уже отсортирован
        if not swapped:
            break
    return arr

# Ввод данных пользователем
arr = list(map(int, input("Введите элементы массива через пробел: ").split()))

sorted_arr = bubble_sort(arr)
print("Отсортированный массив:", sorted_arr)
