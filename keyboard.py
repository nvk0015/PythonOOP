from item import Item

class Keyboard(Item):

    def __init__(self, name:str, price:float, quantity = 0):
        #call the super function to have access to all attributes/methods of the parent class
        super().__init__(
            name, price, quantity
        )