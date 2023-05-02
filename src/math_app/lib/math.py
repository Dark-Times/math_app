import math

class Math():        
    def __init(self, val1, val2):
        self.val1 = val1
        self.val2 = val2

    def AddTwoValues(self, val1, val2):
        return int(val1) + int(val2)

class Addition():
    def AddTwoValues(val1, val2):
        return int(val1) + int(val2)

class Multiplication():
    def Multiply(val1, val2):
        return int(val1) * int(val2)
        
class Division():
    # Custom object initialiser
    def __init__(self, val1, val2, result):
        super().__init__(val1,val2)
        self.result = int(result)
    
    def DivideBy():
        self.result = int(self.val1) / int(self.val2)