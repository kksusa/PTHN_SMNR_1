def CheckNumbers(param1):
    while True:
        try:
            number = int(input(f"{param1} "))
            if number != 0:
                return number
            else:
                print("Координата точки введена неправильно.")    
        except:
            print("Координата точки введена неправильно.")

def QuarterDefenition(x,y):
    if x > 0 and y > 0: print ("Это 1-ая четверть.")
    elif x < 0 and y > 0: print ("Это 2-ая четверть.")
    elif x < 0 and y < 0: print ("Это 3-ая четверть.")
    else: print ("Это 4-ая четверть.")

x = CheckNumbers("Введите координату X, отличную от нуля:")
y = CheckNumbers("Введите координату Y, отличную от нуля:")
QuarterDefenition(x, y)