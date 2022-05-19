#----------------
#ArithemticStack.py is a script file that contain function "arith()" that i wrote to execute F(x) coming from functionplotter.py
#The algorithm to execute F(x) is based on using two Stacks data structures, one for operations
# and the other for numbers 
#----------------

#function to determine the priority of the operator passed
def OpPriority(c):
    switcher = {
        '+' : 1,
        '-' : 1,
        '/' : 2,
        '*' : 2,
        '^' : 3
    }
    return switcher.get(c,0)

#function to simply calculate x1 (op) x2 and return the result
def calculate(x1,x2,op):
    prior = OpPriority(op)
    if(prior == 1):
        if(op == '+'):
            return int(x1)+int(x2)
        else:
            return int(x1)-int(x2) 
    elif(prior == 2):
        if(op == '*'):
            return int(x1)*int(x2)
        else:
            return int(int(x1)/int(x2))
    else:
        return int(pow(int(x1),int(x2)))

#function to evalute different operands together such as vectors with vectors, vectors with numbers and numbers with numbers 
def evaluate(x1,x2,op):
    isX1List = isinstance(x1,list)
    isX2List = isinstance(x2,list)
    if(isX1List and isX2List):
        res = []
        for i in range(len(x1)):
            res.append(calculate(x1[i],x2[i],op))
        return res
    elif(isX1List):
        res = []
        for i in range(len(x1)):
            res.append(calculate(x1[i],x2,op))
        return res        
    elif(isX2List):
        res = []
        for i in range(len(x2)):
            res.append(calculate(x1,x2[i],op))
        return res
    else:
        return calculate(x1,x2,op)        

#main arith() function that does all the magic
def arith(fn,x):
    """Calculate arithmetic statement fn of variable x
        return list y with result of function 
        ex:
        arith("3*x",x=[1,2,3,4])
        //output  y=[3,6,9,12]
    """
    i = 0       #counter
    stackVal = []   #stackA holds values
    stackOp = []    #stackB holds operators
    while(i < len(fn)):
        c = fn[i]   
        if(c.isdigit()):    #if char of fn is a digit push to stackA 
            while(i < len(fn)-1 and fn[i+1].isdigit()):
                i += 1
                c += fn[i]
            stackVal.append(c)
        elif(OpPriority(c)): #if it is operator then push to stackB
            if(not OpPriority(fn[i-1])):
                while(len(stackOp) and OpPriority(c) <= OpPriority(stackOp[len(stackOp)-1])): #if priority of operator existed in stack is higher then evaluate what's in stackA
                    x2 = stackVal.pop()
                    x1 = stackVal.pop()
                    op = stackOp.pop()
                    stackVal.append(evaluate(x1,x2,op))
                stackOp.append(c)
            else: #double signs detected 
                return "Syntax Error"
        elif(c == 'x'):
            stackVal.append(x) #add to stackA vector x (x-axis)
        else:
            #wrong variable detected
            #return syntax error to plotter script

            return "Syntax Error, Wrong Variable"
        i += 1

    while(len(stackOp)): #evaluate what is left in StackA
        x2 = stackVal.pop()
        x1 = stackVal.pop()
        op = stackOp.pop()        
        stackVal.append(evaluate(x1,x2,op))
    res = stackVal.pop()
    if(not isinstance(res,list)):
        arr = [] 
        for i in range(len(x)):
            arr.append(int(res))
        res = arr
    return res  #return final result vector y[] (y-axis)
