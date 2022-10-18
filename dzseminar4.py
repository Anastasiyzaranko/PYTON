# Вычислить число c заданной точностью d

# Пример:

# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

# import math
# i=int(input(" введите кол-во знаков после запятой : "))
# while i < 1 or i > 10:
#     i=int(input(" введите кол-во знаков после запятой : "))
# else:
#     print(10**-i,round(math.pi,i),sep="->")    


# Задайте натуральное число N. Напишите программу, которая составит список
#  простых множителей числа N.

# num = int(input(" введите число : "))
# count = []
# i = 2 
# while i<=num:
#     if num % i == 0:
#         count.append(i)
#         num=num//i
        
#     else:
#         i+=1    
# print(count,end=",")


# Задайте последовательность чисел. Напишите программу, которая выведет список 
# неповторяющихся элементов исходной последовательности.
# num = [15 , 17 ,3 , 2, 5 ,15 ,2]
# nam = []
# for i in num:
#     if num.count(i)==1:# кол-во раз в строке = 1 
#         nam.append(i) # добовляем 
# print(nam)        




# Задана натуральная степень k. Сформировать случайным образом список коэффициентов
#  (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

# Пример:

# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
# from random import randint, random

# k= int(input(" введите степень : "))
# kof = list() # список коэффиц.
# for i in range(1,k+2):
#     kof.append(randint(1,100))

# ans= list()    

# for  i in range(len(kof)):
#     if k == 1:
#         ans.append (f"{kof[i]}*x")
#     elif  k == 0:
#         ans.append (f"{kof[i]}")  
#     else:
#         ans.append (f"{kof[i]}*x**{k}")
#     flag=randint(0,1)
#     if flag == 1:
#         ans.append("+")  
#     elif flag == 0:
#         ans.append("-")
#     k-=1
# ans.pop(-1)
# ans.append("=0")  
# fout= open ("output.txt","w")  
# fout.write("".join(ans))  
# fout.close  




# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать 
# файл, содержащий сумму многочлен


 
