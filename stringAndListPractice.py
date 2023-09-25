words = "It's thanksgiving day. It's my birthday,too!"

wordList = words.find("day")
print(wordList)
words = words.replace("day", "month")
print(words)

myList = ["hello",2,54,-2,7,12,98,"world"]
print(myList[0], myList[len(myList)-1] )

def listFilter(x):
    if isinstance(x,str):
        return x
newList = filter(listFilter, myList)
print(newList)

numList = [19,2,54,-2,7,12,98,32,10,-3,6]
numListSorted = sorted(numList)
print(numListSorted)
    
numListA = numList[:len(numList)//2]
numListB = numList[len(numList)//2:]
print(numListA, numListB)
numListA.insert(0,numListB)
print(numListA)