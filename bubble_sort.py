def bubble(m):
    for j in range(len(m)-1):
        t=1
        for i in range(len(m)-1):
            if m[i]>=m[i+1]:
                m[i],m[i+1]=m[i+1],m[i]
                t=0
        if t==1:
            break
    return m

num = [10,6,8,9,2,11,7,4,6,1]
print(bubble(num))