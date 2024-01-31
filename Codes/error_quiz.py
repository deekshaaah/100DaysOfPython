a = input("Enter  an integer :  ")


if (a == "quiz"):
    print("No error!")
    
elif (int(a)<0):
    raise ValueError("Value should be a positive integer!")

else:
    print("Enter something valid")
