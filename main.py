## used to create instances and work with data###

from item import Item
from phone import Phone
from keyboard import Keyboard

item1 = Item('Laptop',500, 2)
print('The price is: ', item1.calculate_total_price())

print(item1.name)
item1.name = 'Laptop2'
print(item1.name)

#item1.price = 900
print(item1.price)

print(item1.apply_discount(0.2))

# item1.send_email()

phone1 = Phone('SamsungA71',350.0,2)
print(phone1.price)


##Implementation of Polymorphism
print(phone1.apply_discount(0.2)) # apply_discount was declared in Item class but 
#being used in Phone class, an example for polymorphism

keyboard1 = Keyboard('DeutschKeypad', 500, 2)
print(keyboard1.apply_discount(0.2))
