def countCurrency(amount): #определяем функцию её аргумент.
    money = [1000, 500, 200, 100, 50, 20, 10, 5, 3, 2, 1]
    print ("Количество банкнот и их номинал ->")
    for i in money:
        if amount >= i:
            j = amount // i
            amount = amount - j * i
            print (i, ":", j)
amount = int(input("Введите сумму которую хотите снять ->"))
countCurrency(amount) #обращение к функции