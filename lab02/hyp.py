import math

def hyp(a,b):
    hyp = math.sqrt(a**2 +b**2)
    return hyp

def distance(x1,x2,y1,y2):
    dist = math.sqrt((x2-x1)**2+(y2-y1)**2)
    return dist
    
def odd_numbers(a,b):
    for number in range(a,b):
        if number%2 != 0:
            print(f"Odd number in range: {number}")
            
print('=======================================================')
print(f"hyp of 3,4 kat = {hyp(3,4)}")
print()
print('=======================================================')
print(f"dist between 1,3 and 2,2 = {distance(1,3,2,2)}")
print()
print('=======================================================')
odd_numbers(1,10)
