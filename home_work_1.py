class Fraction:

     def __init__(self, num, denum):
         if denum == 0:
             raise ValueError('Denum cant be 0!')
         self.num = num
         self.denum = denum

     def add(self, other):
         num = self.num * other.denum + other.denum * self.denum
         denum = self.denum * other.denum
         print(num)
         print("-")
         print(denum)



     def subract(self, other):
        num = self.num * other.denum - other.denum * self.denum
        denum = self.denum * other.denum
        print(num)
        print("-")
        print(denum)

     def mltpl(self, other):
        num = self.num * other.num
        denum = self.denum * other.denum
        print(num)
        print("-")
        print(denum)

     def dvd(self, other):
        num = self.num * other.denum
        denum = self.denum * other.num
        print(num)
        print("-")
        print(denum)


fraction1 = Fraction(5, 2)
fraction2 = Fraction(8, 5)
fraction1.add(fraction2)

print( )

fraction1 = Fraction(5, 2)
fraction2 = Fraction(8, 5)
fraction1.subract(fraction2)

print(  )

fraction1=Fraction(5, 2)
fraction2 = Fraction(8, 5)
fraction1.mltpl(fraction2)

print( )

fraction1 = Fraction(5, 2)
fraction2 = Fraction(8, 5)
fraction1.dvd(fraction2)