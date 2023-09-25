def say_hello(name):
    #these lines are indented therefore part of the function
  if name:
   print( 'Hello, ') + name + ' from inside the function'
  else:
   print ('No name')
# now we're unindented and have ended the previous block
print ('Outside of the function')
say_hello("Zen")

myList = ["alpha", "beta", "charley", "delta"]
for element in myList:
    print("Hello ", element)

for count in range(0,5):
    print("Looping ", count)
    
count = 0    
while count < 5:
    print("Looping ", count)
    count+=1
    
for val in "string":
    if val == "i":
        break
    print (val)