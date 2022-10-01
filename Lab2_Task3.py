class Product:
    def __init__(self, price, description):
        if price < 0:
            raise ValueError
        if not isinstance(price, (int, float)):
            raise TypeError("Price isn't a number")
        self.price = price
        self.description = description


class Customer:
    def __init__(self, surname, name, mobile_phone):
        if not isinstance(mobile_phone, (int, float)):
            raise TypeError("Mobile phone isn't a number")
        self.surname = surname
        self.name = name
        self.mobile_phone = mobile_phone


class Order:
    def __init__(self, customer, *product):
        if not isinstance(customer, Customer):
            raise TypeError("There is no customer")
        for i in product:
            if not isinstance(i, Product):
                raise TypeError("There is not only products")
        self.customer = customer
        self.products = product
        self.money = 0

    def __Calculate_Order(self):
        self.money = 0
        for i in self.products:
            self.money += i.price
        return self.money

    def __str__(self):
        return f'The price of order for {self.customer.surname} {self.customer.name} is {self.__Calculate_Order()}'


boy = Customer("Yevheniy", "Zdesenko", 380971610252)
apple = Product(3, "Apple")
pineapple = Product(5, "Pineapple")
peach = Product(2, "Peach")
order = Order(boy, apple, pineapple)
print(order)
