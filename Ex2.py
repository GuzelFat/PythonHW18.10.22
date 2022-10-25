# 2. Задайте натуральное число N. Напишите программу,
#  которая составит список простых множителей числа N.



# N=int(input("Введите число: "))
# a=[]
# p=0
# for j in range (1, N+1):
#     if(N%j==0):
#         #a.append(j)
#         for i in range (1, j+1):
#             if j%i==0:
#                 p+=1
# if p==2:
#     a.append(j)
# # print ("Все делители", N, ":", a)

# # for i in range (1, j+1):
# #     if j%i==0:
# #         p+=1
# #         if p>2:
# #             a.remove(j)
# print ("Простые делители", N, ":", a)

# #         p+=1
# #         for j in range (1, N+1):
# #             if (N%j==0):
# #                   if p==2:
# #                     a.append(j)
        
# # print (a)

# N=int(input("Введите число: "))
# a=[]
# p=0
# for i in range (1, N+1):
#     for j in range (1,i+1):
#         if i%j==0:
#             p+=1
#         if p==2:
#             if N%i==0:
#                 a.append(i)
# print (a)

# N=int(input("Введите число: "))
# a=[]
# p=0
# j_prost=0
# for j in range (1, N+1):
#     for i in range (1, j+1):
#         if j%i==0:
#             p=p+1
#             if p<=2:
#                 j_prost=1   
#     if N%j==0 and j_prost==1:
#         a.append(j)
# print (a)
 


# n = int(input())
# a =[]
# p=0
# for i in range (1, n+1):
#     for j in range (1, i+1):
#         if i%j==0:
#             p+=1
#     if n%i==0 and p==2:
#         a.append(i)
# print (a)


n = int(input())
a =[]
for i in range (1, n+1):
    if n%i==0:
        p = 0
        for j in range(1,i+1):
            if i%j==0:
                p+=1
        if p<=2:
            a.append(i)
print(a)
