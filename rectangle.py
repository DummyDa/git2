class Rectangle():
    def __init__(self, a, b):
        self.a = a
        self.b = b     
        
    def ploshad(self):
        return self.a * self.b
    
    def perimeter(self):
        return self.a * 2 + self.b * 2