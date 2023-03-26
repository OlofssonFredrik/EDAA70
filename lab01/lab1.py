import math

def sum(x1,x2):
    res = x1+x2
    return res

def farenheit(celcius):
    faren = (9*celcius/5)+32
    return faren
    
def celcius(farenheit):
    celc = 5/9*(farenheit-32)
    return celc

def area(diameter):
    A = math.pi*diameter**2/4
    return A

def switch(a,b):
    a,b = b,a
    return a,b

def for_loop(a,b):
    for i in range(a,b):
        print(i)
        
def sqrt(inputvalue):
    sqrtval = math.sqrt(inputvalue)
    return sqrtval

def loop_degrees(start,stop):
    for deg in range(start,stop):
        print(f"Celcius: {deg}")
        print(f"Farenheit: {farenheit(deg)}")
    return None

print('===============================================================================================================')
print(f"25degrees Celcius = {farenheit(25)} degrees Farenheit, 100 degress Farenheit = {celcius(100)} degrees Celcius")
print()
print('===============================================================================================================')
print(f"Area diameter 5cm = {area(5)} cm^2, Area diameter 10cm = {area(10)} cm^2")
print()
print('===============================================================================================================')
print(f"Byt plats på 5 och 7. {5,7} = {switch(5,7)}")
print()
print('===============================================================================================================')
print(f"{for_loop(5,16)}")
print()
print('===============================================================================================================')
print(f"Sqrt 10: {sqrt(10)}")
print()
print('===============================================================================================================')
print(f"Printing Degrees between 10-20: {loop_degrees(10,21)}")
print()
print('===============================================================================================================')
