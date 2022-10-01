class Rectangle:
    def __init__(self, len = 1, wid = 1):
        self.length = len
        self.width = wid

    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, len):
        if not(len > 0 and len < 20):
            raise ValueError("Len not in range [0,20]");
        if not (isinstance(len, (float, int))):
            raise TypeError("Len isn't a float");
        self.__length = len

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, wid):
        if not (wid > 0 and wid < 20):
            raise ValueError("Wid not in range [0,20]");
        if not (isinstance(wid, (float, int))):
            raise TypeError("Wid isn't a float");
        self.__width = wid

    def perimetr(self):
        return 2 * (self.length + self.width)

    def area(self):
        return self.length * self.width


x = Rectangle(5.3, 9.4)
print(x.area())
print(x.perimetr())

