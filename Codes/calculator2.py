a = int(input("Enter a number "))
b = int(input("Enter another number "))

x = int(input(""" 1. Addition
2. Subtraction
3. Multiplication
4. Division

Enter a number between 1 to 4 """))

match x:
    case 1:
        print("Sum is", a+b)

    case 2:
        print("Difference is ", a-b)

    case 3:
        print("Product is ", a*b)

    case 4:
        print("Division is ",a/b)

        

    

