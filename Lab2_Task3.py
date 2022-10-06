class Product:
    def __init__(self, price, description):
        if price < 0:
            raise ValueError
        if not isinstance(price, (int)):
            raise TypeError("Price isn't a number")
        self.price = price
        self.description = description

    def __str__(self):
        return f'The price of {self.description} is {self.price}'

class Customer:
    def __init__(self, surname, name, mobile_phone):
        if not isinstance(mobile_phone, (int, float)):
            raise TypeError("Mobile phone isn't a number")
        self.surname = surname
        self.name = name
        self.mobile_phone = mobile_phone

    def __str__(self):
        return f'The customer is {self.surname} {self.name}, phonenumber is {self.mobile_phone}'

class Order:
    def __init__(self, customer, *product):
        if not isinstance(customer, Customer):
            raise TypeError("There is no customer")
        for i in product:
            if not isinstance(i, Product):
                raise TypeError("There is not only products")
        self.customer = customer
        self.products = []
        self.products_quantity = []
        for i in product:
            self.Add_Product(i)
        self.money = 0

    def Add_Product(self, product):
        if product in self.products:
            self.products_quantity[self.products.index(product)] += 1
        else:
            self.products.append(product)
            self.products_quantity.append(1)

    def Delete_Product(self, product):
        if product in self.products:
            if self.products_quantity[self.products.index(product)] > 1:
                self.products_quantity[self.products.index(product)] -= 1
            else:
                self.products.pop(self.products.index(product))
    def __Calculate_Order(self):
        self.money = 0
        for i in self.products:
            self.money += i.price * self.products_quantity[self.products.index(i)]
        return self.money

    def __str__(self):
        return f'The price of order for {self.customer.surname} {self.customer.name} is {self.__Calculate_Order()}'


boy = Customer("Yevheniy", "Zdesenko", 380971610252)
apple = Product(3, "Apple")
print(apple)
print(boy)
pineapple = Product(5, "Pineapple")
order = Order(boy, apple, apple)
order.Add_Product(apple)
order.Add_Product(pineapple)
order.Delete_Product(apple)
print(order)
