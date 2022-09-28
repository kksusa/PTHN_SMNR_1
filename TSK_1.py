def CheckNumbers(param1):
    while True:
        try:
            number = int(input(f"{param1} "))
            if number >= 1 and number <= 7:
                return number
            else:
                print("Число введено неправильно.")    
        except:
            print("Число введено неправильно.")

def DayOfWeek(param2):
    if param2 >= 1 and param2 <= 5:
        print("День не является выходным.")
    else:
        print("Ура! Выходной!")         

DayOfWeek(CheckNumbers("Напишите целое число от 1 до 7:"))