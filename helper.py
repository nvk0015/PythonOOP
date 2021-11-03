#When to use static methods and when to use class methods


class Item:
    @staticmethod
    def is_integer(num):
        '''
        This should do something that has relationship with the class,
        but not something that must be unique per instance!
        '''

    @classmethod
    def instantiate_from_something():
        '''
        This should also do something that has relationship 
        with the class, but ususally, those are used to
        manipulate different structures of data to instantiate
        objects, like we have done with CSV
        '''