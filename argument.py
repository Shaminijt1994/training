def my_var(v1,v2,v3):
    v1=int(input("v1="))
    v2=int(input("v2="))
    v3=int(input("v3="))
    if(v1 == 1):
        print("The polygon is a square")
    else:
        print("Try Again")
    
def myFun(*argv):
    print("Name is " + str(argv[0]))
    print("age is " + str(argv[1]))
    print("city is " + str(argv[2]))
    print("phone is " + str(argv[3]))
 
 
myFun('30', 'shamu', 'tvm', 'phone')

#myFun(10) => 100
#myFun(10, 20) => 200
#myFun(10, 20, 30) => sdasd