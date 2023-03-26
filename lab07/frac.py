
def gcd(a,b):
    abs_a = abs(a)
    while b != 0:
        t = b
        b = a % b
        a = t
    
    return abs_a, a   

_, dela = gcd(3,9)

class Frac:
    def __init__(self,numer,denom):
        
        _,dela = gcd(numer,denom)
        
        self.numer = int(numer/dela)
        self.denom = int(denom/dela)
        
    def __str__(self):
        return f"{self.numer}/{self.denom}"
    
    def __add__(self, other):
        num = self.numer*other.denom + self.denom*other.numer
        den = self.denom*other.denom
        return Frac(num, den)
        
    def __sub__(self,other):
        num = self.numer*other.denom - self.denom*other.numer
        den = self.denom * other.denom
        return Frac(num,den)  
    
    def __mul__(self,other):
        num = self.numer*other.numer
        den = self.denom * other.denom
        return Frac(num,den)  
    
    def __truediv__(self,other):
        num = self.numer*other.denom
        den = self.denom * other.numer
        return Frac(num,den)  
    

sum = Frac(1,3) + Frac(1,3)
print(sum)

#print(1/3+1/3+1/6*1/6)           
#    
#    
#    
##print(Frac().gcd(-2,4))
#x = Frac(1,3)
#print(f"x: {x}")
#y = Frac(1,3)
#print(f"y: {y}")
#z = Frac(1,6)
#print(f"x: {z}")
#w = Frac(1,6)
#print(f"y: {w}")
#
#
#mul = z.mul(w)
#res = x.add(y).add(mul)
#print(res)





