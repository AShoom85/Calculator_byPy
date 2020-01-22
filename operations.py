# Operations

from errors import errors

def operations( num, fun ):

    for i in range(len(fun)):
        
        if ("*" or "/")  in fun :
            
            for t in range(len(fun)):
                
                if "*" in fun:
                    r = fun.index("*")
                    num[r] = str(int(num[r]) * int(num[r+1]))
                    del(num[r+1])
                    del(fun[r])
                    
                elif "/" in fun:
                    r = fun.index("/")
                    num[r] = str(int(num[r]) / int(num[r+1]))
                    del(num[r+1])       
                    del(fun[r])
                    
        else:
            
            for f in range(len(fun)):
                
                if fun[0] == "-":
                    num[0] = str(float(num[0]) - float(num[0+1]))
                    del(num[0+1])
                    del(fun[0])
                elif fun[0] == "+":
                    num[0] = str(float(num[0]) + float(num[0+1]))
                    del(num[0+1])
                    del(fun[0])
                    
    return (num[0])
