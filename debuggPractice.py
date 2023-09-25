def multiply(arr,num):
    newList = []
    for x in arr:
        newList.append(x * num)
    return newList
a = [2,4,10,16]
b = multiply(a,5)
print(b)
# output:
# >>>[2,4,10,16]

