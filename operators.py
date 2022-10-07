#%%
from abc import abstractmethod

class Expression():
    def __repr__(self):
        return str(self)
    def __add__(self, other):
        return Sum(self, other)
    def __mul__(self, other):
        return Product(self, other)
    def __pow__(self, other):
        return Power(self, other)
    def distribute(self):
        return self
    def __eq__(self, other):
        print('Does', self, 'equal', other, '?')
    
class Variable(Expression):
    def __init__(self, letter):
        super().__init__()
        self.operator = False
        self.distributive = False
        self.letter = letter
    def __str__(self):
        return self.letter
    

a = Variable('a')
b = Variable('b')
c = Variable('c')
d = Variable('d')
n = Variable('d')
k = Variable('k')

    
class Operator(Expression):
    def __init__(self):
        super().__init__()
        self.operator = True
        

class Sum(Operator):
    def __init__(self, var1, var2, *args):
        super().__init__()
        self.commutative = True
        self.distributive = True
        self.var1 = var1
        if len(args) > 0:
            self.var2 = Sum(var2, args[0], *args[1:])
        else:
            self.var2 = var2
            
    def __str__(self):
        return f'{str(self.var1)} + {str(self.var2)}'
    def distribute(self):
        return Sum(self.var1.distribute(), self.var2.distribute())
    
class Substract(Operator):
    def __init__(self, var1, var2):
        super().__init__()
        self.commutative = False
        self.distributive = True
        self.var1 = var1
        self.var2 = var2
    def __str__(self):
        return f'{str(self.var1)} - {str(self.var2)}'
    def distribute(self):
        return Substract(self.var1.distribute(), self.var2.distribute())
    
    
class Product(Operator):
    def __init__(self, var1, var2, *args):
        self.commutative = True
        self.distributive = False
        self.var1 = var1
        if len(args) > 0:
            self.var2 = Product(var2, args[0], *args[1:])
        else:
            self.var2 = var2
            
    def __str__(self):
        out1 = f'({self.var1})' if self.var1.distributive else str(self.var1)
        out2 = f'({self.var2})' if self.var2.distributive else str(self.var2)
        return out1 + ' * ' + out2

    def distribute(self):
        if self.var1.distributive:
            return type(self.var1)(
                Product(self.var2, self.var1.var1), 
                Product(self.var2, self.var1.var2)
            ).distribute()
        elif self.var2.distributive:
            return type(self.var2)(
                Product(self.var1, self.var2.var1), 
                Product(self.var1, self.var2.var2)
            ).distribute()
        else:
            return Product(self.var1.distribute(), self.var2.distribute())

class Power(Operator):
    def __init__(self, var1, var2):
        self.commutative = False
        self.distributive = False
        self.var1 = var1
        self.var2 = var2
            
    def __str__(self):
        out1 = f'({self.var1})' if self.var1.distributive else str(self.var1)
        out2 = f'({self.var2})' if self.var2.distributive else str(self.var2)
        return out1 + ' ** ' + out2


# %%
