def palindrome(string):
    if len(string)==1 or len(string)==2:
        return True
    else:
        if string[0]==string[-1]:
            x= string[1:m-1] 
            return palindrome(x)
        else:
            return False

n = input("Enter a string :")
print(palindrome(n))