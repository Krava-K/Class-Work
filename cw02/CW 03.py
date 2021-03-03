#Ввести число, вывести все его делители.
print('Введите число ->')


def printDivisors(n):
    i = 1
    print('Найдено вот сколько делителей ->')
    while i <= n:
        if (n % i == 0):
            print(i)
        i = i + 1

printDivisors(int(input()))
