# Дан массив, состоящий из целых чисел. Напишите
# программу, которая в данном массиве определит
# количество элементов, у которых два соседних и, при
# этом, оба соседних элемента меньше данного. Сначала
# вводится число N — количество элементов в массиве
# Далее записаны N чисел — элементы массива. Массив
# состоит из целых чисел.





arr=list(int(input(f"Enter {i+1} your num:")) for i in range(int(input("Enter num len:"))))
n=len(arr)
result=0
for i in range(1,n-1):
    if arr[i-1] < arr[i] > arr[i+1]:
        result+=1
print(f'Кол-во парных элементов списка = {result}')