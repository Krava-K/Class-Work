print ("Введите два числа, для создания списка!") #вводим граничные значения.
n1 = int(input("Число от которого будет начат отчёт ->")) #начинать нужно только с числа 2
n2 = int(input("Число до которым закончиться отчёт->"))

my_list = list()
for n in range(n1,n2):
    for x in range(n1,n):
        if n%x==0:
            break
    else:
        my_list.append(n)

print('Простые числа из списка!')
print(my_list)
print('Возведём их в квадрат!')

def my_square(num):
    return num ** 2
squared_numbers = list(map(my_square, my_list))

print('Финальный список простых чисел возведённых в квадрат!')
print(squared_numbers)
