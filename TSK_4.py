def CheckNumbers(param):
    while True:
        try:
            number = round(float(input(f"{param} ")), 1)
            return number
        except:
            print("Число введено неправильно.")

def Result(param1, param2):
    while True:
        operand = input("""\nВведите оператор из списка:
\n+: сложение;\n-: вычитание;\n/: деление;\n*: умножение;
mod: взятие остатка от деления;\npow: возведение в степень;
div: целочисленное деление.\n\n""")
        if operand == "+":
            print (f"\n{param1} + {param2} = {param1 + param2}.")
            return()
        elif operand == "-":
            print (f"\n{param1} - {param2} = {param1 - param2}.")
            return()
        elif operand == "/":
            if param2 == 0:
                print("\nДеление на 0 невозможно.")
            else:
                print (f"\n{param1} / {param2} = {round(param1 / param2, 1)}.")
            return()
        elif operand == "*":
            print (f"\n{param1} * {param2} = {round(param1 * param2, 1)}.")
            return()
        elif operand.lower() == "mod":
            print (f"\n{param1} mod {param2} = {round(param1 % param2, 1)}.")
            return()
        elif operand.lower() == "pow":
            print (f"\n{param1} pow {param2} = {round(param1 ** param2, 1)}.")
            return()
        elif operand.lower() == "div":
            print (f"\n{param1} div {param2} = {int(param1 // param2)}.")
            return()
        else:    
            print("\nОператор введен неправильно.")

Result(CheckNumbers("Введите первое число:"), CheckNumbers("Введите второе число:"))