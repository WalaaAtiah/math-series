# The Fibonacci Series
def fibonacci(n):
    """
    this function returns the nth value in the fibonacci numbers  by using recursion function 
    num : int
    return : int
    """
   
    if type(n)!=int or n<0:
        return "you should enter positive number"
    if n == 0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)

   

def fibonacci_iteration(n):
    if type(n)!=int or n<0:
        return "you should enter positive number"
    if n==0:
        return 0
    elif n==1:
        return(1)
    else:
        result=[0,1]
        for i in result:
            if len(result)==n+1:
                 break
            else:
                 result.append(result[len(result)-1] +result[len(result)-2])
        return(result[n])


#The Lucas Numbers:
def lucas(n):
    """
    this function returns the nth value in the lucas numbers  by using recursion function
    num : int
    return : int
    """ 
    if type(n)!=int or n<0:
        return "you should enter positive number"
    if n == 0:
        return 2
    elif n==1:
        return 1
    else:
        return lucas(n-1)+lucas(n-2)

# third requirement :sum series function
def sum_series(n,x=0,y=1):
    """
    this function returns the nth value in the lucas numbers  by using recursion function
    n :int required parameter ,which determine which element in the series to print
    x :int optional parameter the initial value for it is 0
    y :int optional parameter the initial value for it is 1
    return : int
    """ 
    if type(x)!=int and type(y)!=int:
        return "you should enter positive number"
    if type(n)!=int or n<0:
        return "you should enter positive number"
    if n == 0:
        return x
    elif n==1:
        return y
    else:
        return sum_series(n-1,x,y)+sum_series(n-2,x,y)
