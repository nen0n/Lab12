from math import gcd


class Rational:
    def __init__(self, numerator, denominator):
        if denominator == 0:
            raise ZeroDivisionError
        if not isinstance(numerator, int):
            raise TypeError("Wrong arguments")
        if not isinstance(denominator, int):
            raise TypeError("Wrong arguments")
        self.numerator = numerator
        self.denominator = denominator

    def float_form(self):
        return self.numerator / self.denominator

    def ab_form(self):
        return f'{self.numerator // gcd(self.numerator, self.denominator)} / {self.denominator // gcd(self.numerator, self.denominator)}'


x = Rational(1, 4)
y = Rational(2, 4)
print(x.float_form())
print(y.ab_form())

