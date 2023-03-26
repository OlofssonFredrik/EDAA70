def sum(x1,x2):
    res = x1+x2
    return res

def farenheit(celcius):
    faren = (9*celcius/5)+32
    return faren
    
def celcius(farenheit):
    celc = 5/9*(farenheit-32)
    return celc


print(f"25degrees Celcius = {farenheit(25)} degrees Farenheit, 100 degress Farenheit = {celcius(100)} degrees Celcius")