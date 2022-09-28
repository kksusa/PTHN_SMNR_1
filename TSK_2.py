def Comparizon(x,y,z):
    expression1 = not(x or y or z)
    expression2 = not x and not y and not z
    if expression1 == expression2:
        print("Утверждение ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z верно.")
    else:
        print("Утверждение ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z не верно.")  

print("Для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z...")
x = input("введите X: ") 
y = input("введите Y: ") 
z = input("введите Z: ")
Comparizon(x,y,z)