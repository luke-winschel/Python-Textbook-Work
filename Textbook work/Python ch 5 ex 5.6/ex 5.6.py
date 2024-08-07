#Exercise 5.6
#(Functions returning functions) Define a function 'rotate' that receives three arguments and returns a tuple.  Define variables a, b, and c containing 'Doug' 22 and 1984, then call the function 3 times

def rotate ():
    a = 'Doug'
    b = 22
    c = 1984
    
    rotate_tuple = (c, a, b)
    
    print(a)
    print(b)
    print(c)
    
rotate()