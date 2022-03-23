import csv


class Item:
    pay_rate = 0.8
    all = []

    def __init__(self, name: str, price: float, quantity=0):
        #validate using assert
        assert price >= 0
        assert quantity >= 0

        #Assigning to self object
        self.__name = name
        self.price = price
        self.quantity = quantity

        # Actions to execute
        Item.all.append(self)
    @property
    def name(self):
        return self.__name
    def total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate

    @classmethod
    def instantiate_from_csv(cls):

        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:

            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity')),
            )
    
    @staticmethod
    def is_int(num):
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else :
            return False
    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"
        

class Phone(Item):
    all = []
    def __init__(self, name: str, price: float, quantity=0, broken_phone=0):
        super().__init__(name, price, quantity)
        assert broken_phone >= 0

        self.broken_phone = broken_phone

        Phone.all.append(self)

"""
item1 = Item("Phone", 100, 1)
item2 = Item("Laptop", 1000, 3)
item3 = Item("Cable", 10, 5)
item4 = Item("Mouse", 50, 5)
item5 = Item("Keyboard", 75, 5)
"""

#print(Item.__dict__) #All attributes (Class Level)
#print(item1.__dict__) #All attributes (instence level)
"""
"""
# i = instance

#Item.instantiate_from_csv()
#print(Item.all)
phone1 = Phone("Iphone", 500, 5, 1)
item = Item("Item", 500)
#item.name = "Name"
print(item.name)
# print(Item.is_int(8.0))