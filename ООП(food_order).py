from abc import ABC, abstractmethod


class MenuItem(ABC):
    def __init__(self, name, price, discount):
        self.name = name
        self._price = price
        self._discount = discount

    @property
    def get_price(self):
        return self._price

    @abstractmethod
    def get_final_price(self):
        pass


class Drinks(MenuItem):

    def get_final_price(self):
        return self._price * (1 - (self._discount+5) / 100)

    def __str__(self):
        return self.name


class MainCourse(MenuItem):

    def get_final_price(self):
        return self._price * (1 - (self._discount + 10) / 100)


class Order:
    def __init__(self):
        self.order = []
        self.drinks = {}
        self.food = {}

    def item_to_order(self, item: MenuItem):
        if isinstance(item, MenuItem):
            self.order.append(item)
            print(f"{item.name} добавлен в меню")
            if isinstance(item, Drinks):
                if item.name not in self.drinks:
                    self.drinks[item.name] = []
                self.drinks[item.name].append(item.get_final_price())
            elif isinstance(item, MainCourse):
                if item.name not in self.food:
                    self.food[item.name] = []
                self.food[item.name].append(item.get_final_price())
        else:
            print(f'{item.name} не найден в меню')

    def remove_item(self, item_name):
        for item in self.order:
            if item.name == item_name:
                self.order.remove(item)

                if isinstance(item, Drinks):
                    del self.drinks[item.name]
                else:
                    del self.food[item.name]

                return f'{item_name} Убран из меню заказа'
        return f'{item_name} еще не заказали'

    def calculate_total(self):
        final_price = 0
        for item in self.order:
            if isinstance(item, Drinks):
                final_price += self.drinks.get(item.name)[0]
            else:
                final_price += self.food.get(item.name)[0]
        return f'Итог: {final_price}'

    def show_bill(self):
        print('-------------------')
        bill = self.food | self.drinks
        print('Ваш заказ: ')
        for name, prices in bill.items():  # prices - это список с ценами
            for price in prices:  # Проходим по списку цен
                print(f'{name} - {price} руб.')
        print(self.calculate_total())
        print('-------------------')


# Создаём объекты напитков и еды
cola = Drinks("Cola", 100, 10)
pizza = MainCourse("Pizza1", 300, 20)
pizza1 = MainCourse("Pizza2", 250, 10)
pizza2 = MainCourse("Pizza3", 150, 20)
# Создаём заказ
order = Order()

# Добавляем элементы в заказ
order.item_to_order(cola)
order.item_to_order(cola)
order.item_to_order(pizza)
order.item_to_order(pizza1)
order.item_to_order(pizza2)

# Пытаемся удалить элемент
print(order.remove_item("Pizza1"))
# Вычисляем общую стоимость
print(order.calculate_total())
order.show_bill()
