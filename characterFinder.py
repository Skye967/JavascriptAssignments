# input
word_list = ['hello','world','my','name','is','Anna']
char = 'o'

def characterFinder(a,b):
    newList = []
    for i in range(0,len(a)):
        if b in a[i]:
            newList.append(a[i])
    return newList
        
    
print(characterFinder(word_list, char))
