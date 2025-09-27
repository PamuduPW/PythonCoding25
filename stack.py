Stack = []

def add():
    t = True
    while t:
        m = input("Enter the data you want to input(To exit enter '/') :")
        if m=='/':
            print("Exited from entering the data")
            n = input("Enter '_' to see the last data or enter '-' to remove the last data :")
            t= False
        else:
            Stack.append(m)
    if n=='_':
        print(see())
    else:
        if n=='-':
            delete()

def delete():
    t = True
    while t:
        n = input("Enter '_' to exit removing data and see the last data :")
        p = Stack.pop()
        if n == '_':
            print("Exited from removing data")
            t = False
            print(see())

def see():
    try:
        return Stack[-1]
    except:
        l = "There's no data to see"
        return l

print("Please enter '+' to input a data")
print("Please enter '-' to remove the last data")
print("Please enter '_' to see the last data")

x = input("What do you want to do with the data('+','-','_') :")
if x=='+':
    add()        
else:
    if x=='-':
        delete()
    else:
        if x=='_':
            print(see())
        else:
            print("Can't recongnize your wants")