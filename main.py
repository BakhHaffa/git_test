a = int(input("number 1: "))
b = int(input("number 2: "))

def addition(a,b):
    sum=a+b
    return int(sum)

def soustraction(a,b):
    sous=a-b
    return int(sous)

def multiplication(a,b):
    times=a*b
    return int(times)

def division(a,b):
    div=a/b
    return int(div)

print("L'addition vaut:", addition(a,b))
print("La soustraction vaut:", soustraction(a,b))
print("La multiplication vaut:", multiplication(a,b))
print("La division vaut:", division(a,b))
