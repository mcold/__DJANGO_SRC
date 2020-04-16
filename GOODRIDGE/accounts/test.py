# coding: utf-8

def bread(func):
    def wrapper():
        print("</--------\>".decode('utf8'))
        func()
        print("<\______/>".decode('utf8'))
    return wrapper

def ingredients(func):
    def wrapper():
        print("#помидоры#".decode('utf8'))
        func()
        print("~салат~".decode('utf8'))
    return wrapper

@ingredients
@bread
def sandwich(food="--ветчина--".decode('utf8')):
    print(food)

sandwich()
