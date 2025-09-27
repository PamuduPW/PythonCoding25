Queue = []

def add():
    t = True
    while t:
        m = input("Enter the data you want to input(To exit enter '/') :")
        if m=='/':
            print("Exited from entering data")
            n = input("Enter '-' to delete the first data or enter '_' to see the data :")
            t = False
        else:
            Queue.append(m)
    if n=='-':
        delete()
    else:
        if n=='_':
            print(see())

def delete():
    t = True
    while t:
        n = input("Enter '_' to exit removing data and see the data or enter anything to skip this :")
        p = Queue.pop(0)
        if n == '_':
            print("Exited from removing data")
            t = False
    print(see())

def see():
    try:
        return f"First data from the list is {Queue[0]} and the last data from the list is {Queue[-1]}"
    except:
        l = "There's no data to see"
        return l

print("Please enter '+' to input a data")
print("Please enter '-' to remove the first data")
print("Please enter '_' to see the last and first data")

x = input("What do you want do with the data('+','-','_') :")
if x=='+':
    add()
else:
    if x=='-':
        delete()
    else:
        if x=='_':
            print(see())
        else:
            print("Can't recognize your wants")