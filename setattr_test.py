import inspect


class Test:

    def __init__(self, attr1, attr2, attr3):
        
        args, _, _, values = inspect.getargvalues(inspect.currentframe())
        values.pop("self") 

        for arg, val in values.items():
            setattr(self, arg, val)

        
    def print(self): 
        print(self.attr1, self.attr2, self.attr3)




test = Test("attribute1", "attribute2", "attribute3") 
test.print()
