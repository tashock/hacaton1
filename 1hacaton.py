import datetime
import json


FILE_PATH = 'products.json'

def get_products():    
    """
    возвращяет сипсок с продуктами
    """
    with open(FILE_PATH) as file:
        product = json.load(file)
    return product
    
def interpretator():
    products = get_products()
    dct = {}
    for i in range(len(products)):
        dct[products[i]['id']] = products[i]
    return dct

def get_one_product(id):
    """
    возвращяет какой-либо продукт по индексу
    """
    product = get_products()
    one_product = [i for i in product if i['id'] == id]
    if one_product:
        return one_product[0]
    return 'Нет такого товара!'
   
def post_product():
    """
    должен создать новый продукт
    """
    

    product = get_products()
    max_id = max([i['id'] for i in product])
    product.append({
        'id': max_id + 1,
        'name': input('Введите имя нового товара: '),
        'Price': float(input('Введите цену нового товара: ')),
        'Date_upload': str(datetime.date.today()),
        'Date_update': str(datetime.date.today()),
        'description': input('Введите описание продукта: '),
        'Status': input('Введите статус товара: ')
        })
    with open(FILE_PATH, 'w') as file:
            json.dump(product, file)
    return 'Добавлен новый продукт!'


def update_product(id):
    """
    должен обновлять уже созданный продукт
    """
    product = get_products()
    product_update = [i for i in product if i['id'] == id]

    if product_update:
        index_ = product.index(product_update[0])
        product[index_]['Status'] = input('Введите статус продукта: ')
        product[index_]['Price'] = input('Введите цену продукта: ')
        product[index_]['Date_update'] = str(datetime.date.today())
        json.dump(product, open(FILE_PATH, 'w'))
        return 'Обновлено!'
    return 'Нет такого товара!'

def delete_product(id):
    """
    Должен удолять продукт по id
    """
    product = get_products()
    product_delete = [i for i in product if i['id'] == id]
    if product_delete:
        product.remove(product_delete[0])
        json.dump(product, open(FILE_PATH, 'w'))
        return 'Товар удален'
    return 'Такого товара'


def filter_price(need, num): 
    dct = interpretator()
    objct = {}
    l = []
    for i in dct:
        objct[dct[i]['name']] = dct[i]['Price']
    items = list(objct.items())
    for item in range(0, len(items)):
        items[item] = list(items[item])
        items[item].reverse()
    if (need == 'ниже'):
        items.sort()
        for i in range(len(items)):
            if items[i][0] <= num:
                l.append(items[i])
            else: 
                continue
    elif (need == 'выше'):
        items.sort()
        for i in range(len(items)):
            if items[i][0] >= num:
                l.append(items[i])
            else: 
                continue
    else:
        return 'Неверные, данные попробуйте снова'
    return l
    
def filter_date_upload(need):
    dct = interpretator()
    date = datetime.datetime.strptime(need, '%Y-%m-%d') 
    objct = {}
    for i in dct:
        if (datetime.datetime.strptime(dct[i]['Date_upload'], '%Y-%m-%d') == date):
            objct[i] = f"{date.day}.{date.month}.{date.year}"
        else:
            continue
    return objct

def filter_status(need):
    dct = interpretator()
    objct = {}
    if (need == 'Sold'):
        for i in dct:
            if (dct[i]['Status'] == 'Sold'):
                objct[i] = dct[i]['Status']
            else:
                continue
    elif (need == 'For sale'):
        for i in dct:
            if (dct[i]['Status'] == 'For sale'):
                objct[i] = dct[i]['Status']
            else:
                continue
    else:
        return 'Неверные данные попробуйте снова'
    return objct


def product_direction():
    while True:
        print('Привет, вот функцонал CRUD: \n1 - получить все товары \n2 - получить определенный товар \n3 - создать товар \n4 - удалить товар \n5 - обновить товар \n6 - фильтер по дате \n7 - фильтер по цене \n8 - фильтер по статусу')
        method = input('Введи число: ')
        if method == '1':
            print(get_products())
        elif method == '2':
            id = int(input('Введи id товара: '))
            print(get_one_product(id))
        elif method == '3':
            print(post_product())
        elif method == '4':
            id = int(input('Введите id товара который хотите удалить: '))
            print(delete_product(id))
        elif method == '5':
            id = int(input('Введите id товара который хотите обновить: '))
            print(update_product(id))
        elif method == '6':
            need = input('Введите дату в формате год-месяц-день: ')
            print(filter_date_upload(need))
        elif method == '7':
            num = int(input('Введите цену по которой хотите фильтровать товар: ' ))
            need = input('Введите ниже/выше: ')
            print(filter_price(need, num))
        elif method == '8':
            need = input('Введите статус товара: ')
            print(filter_status(need))
        else:
            print('Нет такого функционала!')

print(product_direction())
# print(get_products())
# print(get_one_product(2))
# print(post_product())
# print(update_product(1))
# print(delete_product(1))














