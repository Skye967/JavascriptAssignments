list_a = [1,2,5,6,2]
list_b = [1,2,5,6,2]
list_c = [1,2,5,6,5]
list_d = [1,2,5,6,5,3]
list_e = [1,2,5,6,5,16]
list_f = [1,2,5,6,5]
list_g = ['celery','carrots','bread','milk']
list_h = ['celery','carrots','bread','cream']

def compareLists(x,y):
    longer = []
    shorter = []
    if len(x) == len(y):
        longer = x
        shorter = y
    elif len(x) > len(y):
        longer = x
        shorter = y
    else:
        longer = y
        shorter = x
        
    if longer > shorter:
        return "The lists are not the same"
    
    for i in range(0, len(longer)):
        if longer[i] != shorter[i]:
            return "The lists are not the same"
    
    return "Lists are identical"

print(compareLists(list_a, list_b))
print(compareLists(list_d, list_c))
print(compareLists(list_e, list_f))
print(compareLists(list_g, list_h))





