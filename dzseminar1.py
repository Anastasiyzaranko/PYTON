# Напишите программу, которая принимает на вход цифру, обозначающую день недели,
#  и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет


num = int(input("введите число дня недели от 1 до 7 :"))
if num >= 1 and num <=5:
    print(f"{num} - рабочий" )
elif num >=6 and num <= 7:
    print(f"{num} - ураа!! выходной")
      
elif num > 7 or num < 0 :
    print(" введите корректное число от 1 до 7 ")





# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для
#  всех значений предикат.

#---------

# Напишите программу, которая принимает на вход координаты точки (X и Y), 
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта 
# точка (или на какой оси она находится).
# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3


num1 = int(input("введите координаты точки Х : "))
num2 = int(input("введите координаты точки Y : "))
if num1 > 0 and num2 > 0:
    print(f" точка х= {num1} ; y = {num2}  ->  находится в 1  четверти")  
if num1 < 0 and num2 > 0:
    print(f" точка х= {num1} ; y = {num2}  ->  находится в 2  четверти")   
if num1 < 0 and num2 < 0:
    print(f" точка х= {num1} ; y = {num2}  ->  находится в 3  четверти")    
if num1 > 0 and num2 < 0:
    print(f" точка х= {num1} ; y = {num2}  ->  находится в 4  четверти")   
elif num1 == 0 or num2 == 0 :
    print(" X или  Y  не должны быть равны 0 ")      



# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных 
# координат точек в этой четверти (x и y).

num = int(input("введите номер четверти: "))

if num == 1:
    print("диапазон возможных координат точек в этой четверти x > 0 и y > 0" )
elif num == 2:
    print("диапазон возможных координат точек в этой четверти x < 0 и y > 0" )
elif num == 3:
    print("диапазон возможных координат точек в этой четверти x < 0 и y < 0" )
elif num == 4:
    print("диапазон возможных координат точек в этой четверти x > 0 и y < 0" )    
elif num < 0 or num > 4:
    print("введите корректное число, от 1 до 4 " )    


# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние 
# между ними в 2D пространстве.

# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

x1 = int(input("введите координаты точки Х1 : ")) 
y1 = int(input("введите координаты точки y1 : "))
x2 = int(input("введите координаты точки Х2 : "))
y2 = int(input("введите координаты точки y2 : "))

num = ((x2-x1)**2 + (y2-y1)**2)**0.5

print( "А",(x1, y1) ," ; ","В",( x2, y2) ," -> " ,format(num,".2f" ),sep = " ")

