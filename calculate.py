from sympy import sympify,symbols, simplify, Symbol

ERROR = -1


def execute(x_axis,eq):
    """execute the equation statement.
    takes two parameters, x_axis: the list of x-axis range numbers, eq: the equation statement
    returns list for successful execution
    returns ERROR for unsuccessful execution 
    """
    #define x as a symbol
    x = Symbol('x')
    #check whether the input statement is correct mathematically
    try:
        #sympify equation
        eq = sympify(eq)
        #check variables
        variables = eq.free_symbols
        #check for undefined symbols
        for var in variables:
            if var != x:
                #there exists undefined variables
                return ERROR
        result = [eq.evalf(subs={x: value},chop=True) for value in x_axis]
        return result
    except:
        #equation is not valid
        return ERROR 