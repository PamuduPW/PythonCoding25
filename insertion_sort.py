def insertion(m):
    val1 = m.pop(0)
    list1 = []
    list1.append(val1)
    while m!=[]:
        element = -1
        val1 = m.pop(0)
        list1.append(val1)
        while list1[element-1]>list1[element]:
            list1[element],list1[element-1] = list1[element-1],list1[element]
            element-=1
    return list1

num = [2,3,9,45,61,51,27,45,32,5,3]
print(insertion(num))