import math

def fooBar():
    
    number = 20
    def isPrime(num):
        flag = False
        for i in range (2, num / 2 + 2):
            if num % i == 0:
                flag = True
                break
        return flag
    
    def isSquare(num):
            if num < 0:
                return False
            square_root = math.sqrt(num)
            if square_root % 1 != 0:
                return False
            return square_root * square_root == num
        
    for i in range(2, 10):
        print(i)
        if isPrime(i) == False:
            print("Foo")
        if isSquare(i) == True:
            print("Bar")
        if isPrime(i) != False and isSquare(i) != True:
            print("FooBar")
    
    
                
print(fooBar())