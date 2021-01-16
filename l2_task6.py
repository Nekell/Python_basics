products = [
    (1, {'название': 'компьютер', 'цена': 20000, 'количество': 5, 'eд': 'шт.'}),
    (2, {'название': 'принтер', 'цена': 6000, 'количество': 2, 'eд': 'шт.'}),
    (3, {'название': 'сканер', 'цена': 2000, 'количество': 7, 'eд': 'шт.'})
    ]
list_number = 4
analytics = {
    'название': set(),
    'цена': set(),
    'количество': set(),
    'eд': set()
    }

while True:
    menu = input('add - Добавить продукт\nlist - Посмотреть список товаров'
                 '\nstat - Посмотреть аналитику\nq - Выход из программы\n')
    if menu == 'q':
        break
    elif menu == 'list':
        for product in products:
            print(product)
    elif menu == 'add':
        name, price, numbers, measure = input('Введите через пробел название, цену,'
                                              'количество и единицу измерения товара: ').split()
        products.append((list_number, {'название': name, 'цена': price, 'количество': numbers, 'eд': measure}))
        list_number += 1
    elif menu == 'stat':
        for product in products:
            analytics['название'].add(product[1]['название'])
            analytics['цена'].add(product[1]['цена'])
            analytics['количество'].add(product[1]['количество'])
            analytics['eд'].add(product[1]['eд'])
        print(analytics['название'])
        print(analytics['цена'])
        print(analytics['количество'])
        print(analytics['eд'])
    else:
        continue
