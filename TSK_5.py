def CheckNumbers(param):
    while True:
        try:
            number = int(input(f"{param} "))
            if number > 0:
                return number
            else:
                print("Число введено неправильно.")    
        except:
            print("Число введено неправильно.")

def PrintArray(array, param):
    for i in range(len(array)):
        print(f"{array[i]}", end = " ")
        if (i + 1) % param == 0: print()

def CreateArrayWithRandomNumbers(m, n):
    import random
    result = []
    for i in range(m*n):
        result.append(random.randint(1, 9))
    return result

def IncreasingArray(array):
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            if (array[i] > array[j]):
                temp = array[i]
                array[i] = array[j]
                array[j] = temp
    print()
    return array

m = CheckNumbers("Введите число строк:")
n = CheckNumbers("Введите число столбцов:")
array = CreateArrayWithRandomNumbers(m, n)
print()
PrintArray(array, n)
PrintArray(IncreasingArray(array), n)