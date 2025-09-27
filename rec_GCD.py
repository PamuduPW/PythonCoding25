def GCD(num1,num2):
    result=num1%num2
    if result==0:
        return num2
    else:
        return GCD(num2,result)

n1 = int(input("Enter the first number :"))
n2 = int(input("Enter the second number :"))

if n2<n1:
    print(f"The GCD between {n1} and {n2} is {GCD(n1,n2)}")
else:
    print(f"The GCD between {n1} and {n2} is {GCD(n2,n1)}")