def isBignumber(x):
    if x > 100:
        return "That's a big number"
    else :
        return "That's a small number"
    
print(isBignumber(102))
print(isBignumber(99))

def isLongSentence(x):
    if len(x) > 10:
        return "Long sentence"
    else:
        return "Short Sentence"
    
print(isLongSentence("Hello my name is slim shady."))
print(isLongSentence("No name."))

def isLongList(x):
    if len(x) > 10:
        return "Big List!"
    else:
        return "Short List."
    
print(isLongList([1,2,3,4,5,6,7,8,9,10,11]))
print(isLongList([1,2,3,4,5]))