from item import Item

class Phone(Item):

    def __init__(self, name:str, price:float, quantity = 0, broken_phones=0):
        #call the super function to have access to all attributes/methods of the parent class
        super().__init__(
            name, price, quantity
        )
        ##Run validations to received arguments
        assert broken_phones>=0, f'Broken Phones {broken_phones} is not greater than or equal to zero'
        ## Assign to self object
        self.broken_phones = broken_phones