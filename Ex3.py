# 3. Задайте последовательность чисел. Напишите программу,
#  которая выведет список неповторяющихся элементов исходной последовательности.

# 
b= input("Задайте последовательность: ").split()
c=[]
for i in b:
    if i not in c:
        c.append(i)
print(c)

