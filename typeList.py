#input
l = ['magical unicorns',19,'hello',98.98,'world']
#input
# input
t = [2,3,1,7,4,12]

# input
y = ['magical','unicorns']

def typeList(a):
    thisString = ""
    sum = 0
    containsNumber = 0
    containsString = ""
    
    for x in range(0,len(a)):
        type = isinstance(a[x], str)
        if type == True:
            thisString += a[x]
            containsString = True
        else:
            sum += a[x]
            containsNumber = True
        
    if containsString == True and containsNumber == True:
        print("The list you entered is of mixed type.")
        print("String: " + thisString)
        return "Sum: " + str(sum)
    
    if containsString == True:
        print("The list you entered is of string type.")
        return "String: " + thisString
    
    if containsNumber == True:
        print("The list you entered is of integer type.")
        return "Sum: " + str(sum)
        
        
print(typeList(l))
print(typeList(t))
print(typeList(y))