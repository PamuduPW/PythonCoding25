def selection(m):
    for i in range(len(m)-1):
        t = i
        for j in range(i+1,len(m)):
            if m[t]>m[j]:
                t=j
        n = m.pop(t)
        m.insert(i,n)
    return m

num = [5,9,3,12,7,5,9,6,16,1,8]
print(selection(num))