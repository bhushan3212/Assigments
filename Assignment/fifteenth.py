class Complex :

    def __init__(self, real, img):
        self.real = real
        self.img = img

    @property
    def display(self):
        return f'{self.real}i + {self.img}j'

    def __add__(self, num2):
        self.real = self.real + num2.real
        self.img = self.img + num2.img
        return Complex(self.real,self.img)

    def __sub__(self, num2):
        self.real = self.real - num2.real
        self.img = self.img - num2.img
        return Complex(self.real,self.img)

    def __gt__(self, num2):
            self.real = self.real > num2.real
            self.img = self.img > num2.img
            return True


num1 = Complex(3, 5)
num2 = Complex(1 ,3)
print(num1.display)
print(num2.display)

num4 = num1 - num2
print(num4.display)

print(num1 > num2)

