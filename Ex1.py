# Вычислить число c заданной точностью d
#  Пример:
# при d = 0.001, π = 3.141.  10-1 ≤ d ≤10-10
# π = (4/1) - (4/3) + (4/5) - (4/7) + (4/9) - (4/11) + (4/13) - (4/15) ...

from re import X


def GetIntNumber():
    try:
        x=abs(int(input("Введите целое число N  в диапазоне от 1 до 10, для определения точности ( 10**(-N)) ")))
        return x
    except:
        print("Целое число введено неверно, попробуйте еще раз.")
        return GetIntNumber()
N=GetIntNumber()
while not(1<=N<=10):
    N=GetIntNumber()
d=10**(-N)
Pi=0
x=1
sign=1
while True:
    a=4/x 
    Pi=Pi+sign*a 
    if a<d:
        break 
    sign=sign 
    x=x+2 
print(round(Pi,N))                
