import csv


class Item:
    ##class attribute
    pay_rate = 0.8 #the payrate after 20% discount
    all = []
    def __init__(self, name:str, price:float, quantity = 0):
        ##Run validations to received arguments
        assert price>=0, f'Price {price} is not greater than or equal to zero!'
        assert quantity>=0, f'Quantity {quantity} is no greater than or equal to zero'
        
        ## Assign to self object
        self.__name = name #setting name attribute to a private attribute 
        self.__price = price
        self.quantity = quantity
        self.all.append(self)

    @property
    def price(self):
        return self.__price

    def apply_discount(self, discount_value):
        self.__price = self.__price - self.__price*discount_value
        return self.__price
    def apply_increment(self, increment_value):
        self.__price = self.__price+self.__price*increment_value
        return self.__price
    
    @property   
    #property decorator = Read-only attribute
    def name(self):
        print('You are trying to get some value:: GETTER')
        return self.__name
    
    @name.setter
    #decorator used to reassign values to encapsulated attributes
    def name(self, value):
        print('You are trying to set some value :: SETTER')
        if len(value) >= 10:
            raise Exception('The name is greatrer than 10 characters')
        else:
            self.__name = value

    def calculate_total_price(self):
        return self.__price*self.quantity
    def price_after_discount(self):
        return self.__price*self.quantity*self.pay_rate

    # @classmethod
    # def instantiate_from_csv(cls):
    #     with open('item.csv', 'r') as f:
    #         reader = csv.DictReader(f)
    #         items = list(reader)
    #     for item in items:
    #         Item(
    #             name = item.get('name'),
    #             price=  float(item.get('price')),
    #             quantity= float(item.get('quantity')),
    #             )
    @staticmethod
    def is_integer(num):
        #we will count the floats
        if isinstance(num, float):
            return num.is_integer() #returns num of zeros in decimal values
        elif isinstance(num, int):
            return True
        else:
            return False
    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name},{self.price},{self.quantity}')"
    def __connect(self,smtp_server): #adding __ to make it a private method, sothat we can call them only in this class level
        pass
    def __prepare_body(self):
        return f'''We have {self.name} {self.quantity} times.
        Regards, Vamsi '''
    def __send (self):
        pass 
    def send_email(self):
        self.__connect() 
        self.__prepare_body()
        self.__send()
