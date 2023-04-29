a = int(input("number 1: ")) # La valeur de A sera renvoyée par l'input de l'utilisateur
b = int(input("number 2: ")) # La valeur de B sera renvoyée par l'input de l'utilisateur

def addition(a,b): # On definie la fonction addition
    sum=a+b
    return int(sum)

def soustraction(a,b): # On definie la fonction soustraction
    sous=a-b
    return int(sous)

def multiplication(a,b): # On definie la fonction multiplication
    times=a*b
    return int(times)

def division(a,b): # On definie la fonction division
    div=a/b
    return int(div)

print("L'addition vaut:", addition(a,b))
print("La soustraction vaut:", soustraction(a,b))
print("La multiplication vaut:", multiplication(a,b))
print("La division vaut:", division(a,b))
