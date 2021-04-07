class Complex:

    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        real = self.real + other.real
        imag = self. imag + other.imag
        new_complex = Complex(real, imag)
        return new_complex

    def __sub__(self, other):
        real = self.real - other.real
        imag = self. imag - other.imag
        new_complex = Complex(real, imag)
        return new_complex





c1 = Complex(4, 5)
c2 = Complex(9, 8)
c3 = c1 + c2
print(c3.real)
print(c3.imag)


c1 = Complex(4, 5)
c2 = Complex(9, 8)
c3 = c1 - c2
print(c3.real)
print(c3.imag)


def mulComplex(z1, z2):
    return z1 * z2


# driver code
z1 = complex(2, 3)
z2 = complex(4, 5)

print("Multiplication is :", mulComplex(z1, z2))

def  divComplex(y1, y2):
    return y1 * y2

y1 = complex(2, 40)
y2 = complex(15, 55)
print("Division is :", divComplex(y1, y2))

