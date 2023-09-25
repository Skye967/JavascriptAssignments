def checkerBoard():
    for i in range(0,7):
        if i % 2 == 0:
            print("* * * * ")
        else:
            print(" * * * *")
            
print(checkerBoard())