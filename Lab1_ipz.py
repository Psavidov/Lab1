a = int(input("Введіть кількіть елементів в послідовності Фібоначчі: "))
b = [0,1]
n = a-2
l = 0
if a<0:
    print("Кількість елементів має бути невід'ємним числом")
elif type(a) != int:
    print("Число має бути цілим")
elif a == 0:
    b = []
    print(b)
elif a == 1:
    b = [0]
    print(b)
elif a == 2:
    b = [0,1]
    print(b)
else:
    while n>0:
        n-=1
        l = b[-1] + b[-2]
        b.append(l)
    print(b)
