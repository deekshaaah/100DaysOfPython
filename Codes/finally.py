# finally is ALWAYS executed.
# the main difference between print() and finally is that if you want to break a database connection, if an error occured in which you want to revoke the database connection or you want to clean up a file or you want to close a file on which you were performing the functions, for work like this you HAVE to use finally irrespective of whether it is in try or except  
def fun1():
    try:
        l = [1, 2, 3]
        i = int(input("Enter the index : "))
        print(l[i])
        return 1

    except:
        print("Some error occured")
        return 0

    finally:
         print("This statement is always executed")

a = fun1()
print(a)
