def gr(a,b):
    if (a > b):
        print(a, "is greater than ", b)

def odd(a,b):
    if (a%2 != 0 or b%2 != 0):
        print("Either", a, "or", b, "is odd.")
        
c =int(input("Enter first number "))
d = int(input("Enter second number "))

gr(c,d)

odd(c,d)
    
