def gcd(m,n):
    while m%n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm%oldn
    return n

class Fraction:

    def __init__(self,top,bottom):
        if type(top) != int or type(bottom) != int:
            raise RuntimeError("Both numerator and denominator must be integers")
        else:
            self.num = top//gcd(top,bottom)
            self.den = bottom//gcd(top,bottom)

    def getNum(self):
        return self.num
    def getDen(self):
        return self.den

    def __str__(self):
        return str(self.num)+"/"+str(self.den)

    def __repr__(self):
        return "Fraction(%d,%d)" % (self.num,self.den)

    def show(self):
        print(str(self.num)+"/"+str(self.den))

    def __add__(self,otherfraction):
        newnum = self.num*otherfraction.den + \
                      self.den*otherfraction.num
        newden = self.den * otherfraction.den
        return Fraction(newnum,newden)

    def __radd__(self,otherfraction):
        newnum = self.num*otherfraction.den + \
                      self.den*otherfraction.num
        newden = self.den * otherfraction.den
        return Fraction(newnum,newden)

    def __iadd__(self,otherfraction):
        newnum = self.num*otherfraction.den + \
                      self.den*otherfraction.num
        newden = self.den * otherfraction.den
        self.num = newnum
        self.den = newden
        return Fraction(self.num,self.den)
    
    def __sub__(self,otherfraction):
        newnum = self.num*otherfraction.den - \
                      self.den*otherfraction.num
        newden = self.den * otherfraction.den
        return Fraction(newnum,newden)

    def __mul__(self,otherfraction):
        newnum = self.num*otherfraction.num
        newden = self.den*otherfraction.den
        return Fraction(newnum,newden)

    def __truediv__(self,otherfraction):
        newnum = self.num*otherfraction.den
        newden = self.den*otherfraction.num
        return Fraction(newnum,newden)

    def __eq__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den
        return firstnum == secondnum

    def __gt__(self, other):
        if self.num*other.den > self.den*other.num:
            return True
        else:
            return False

    def __lt__(self, other):
        if self.num*other.den < self.den*other.num:
            return True
        else:
            return False

    def __ge__(self, other):
        if self.num*other.den >= self.den*other.num:
            return True
        else:
            return False

    def __le__(self, other):
        if self.num*other.den <= self.den*other.num:
            return True
        else:
            return False

    def __ne__(self, other):
        if self.num*other.den != self.den*other.num:
            return True
        else:
            return False

x = Fraction(1,2)
y = Fraction(2,3)
print(x+y)
print(x == y)
