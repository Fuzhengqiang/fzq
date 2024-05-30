class Counterlist(list):
    def __init__(self,*x):
        super().__init__(*x)
        self.counter = 0
    def __getitem__(self, index):
        self.counter += 1
        return super().__getitem__(index)
cl = Counterlist(range(10))
print(cl[4],cl[3],cl.reverse(),cl.index(4),cl.counter)

class Rectangle:
    def __init__(self):
        self.width = 0
        self.height = 0
    def setitem(self, size):
        self.width,self.height = size
    def getitem(self):
        return self.width,self.height
    size = property(getitem,setitem)
re = Rectangle()
re.size = 9,9
re.width = 10
print(re.width,re.height)

class MyClass:
    @staticmethod
    def smeth():
        print('This is a static method')
    @classmethod
    def cmeth(cls):
        print('This is a class method of',cls)
MyClass.smeth()
MyClass.cmeth()

class Rectangle:
    def __init__(self):
        self.width = 0
        self.height = 0
    def __setattr__(self, name, value):
        if name == 'size':
            self.width,self.height = value
        else:
            self.__dict__[name] = value
    def __getattr__(self, name):
        if name == 'size':
            return self.width,self.height
        else:
            raise AttributeError()
re = Rectangle()
re.name()