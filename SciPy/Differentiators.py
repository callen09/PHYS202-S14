import numpy as np

def fourPtCDiff(x,y,h):
    """
    Takes a function y(x) and returns the derivative of it
    at a central point by determining the slope of from two points above
    and two points below it. 
    Special code is used for the end points in the data.
    
    x is an array.
    y is a function of x.
    h is the spacing of the values.
    """
    dydx = np.zeros(y.shape,float)
    dydx[2:-2] = (y[0:-4]-8*y[1:-3]+8*y[3:-1]-y[4:])/(12*h)
    dydx[-2] = (y[-4]-8*y[-3]+8*y[-1]-y[0])/(12*h)
    
    dydx[1] = (y[2]-y[1])/(x[2]-x[1]) 
    dydx[0] = (y[1]-y[0])/(x[1]-x[0]) 
    dydx[-1] = (y[-1]-y[-2])/(x[-1]-x[-2])
    
    return dydx
    
def twoPtFDiff(x,y):
    """
    Takes a function y(x) and returns the derivative of it
    using two data points to determine the slope between them. 
    
    x is an array.
    y is a function with x as the independent variable.
    """
    dydx1 = np.zeros(y.shape,float)
    dydx1[0:-1] = np.diff(y)/np.diff(x)
    dydx1[-1] = (y[-1]-y[-2])/(x[-1]-x[-2])
    return dydx1

    
def twoPtCDiff(x,y):
    """
    Takes a function y(x) and returns the derivative of it
    at a central point by determining the slope of from the point above
    and below it. Special code is used for the end points in the data.
    
    x is an array.
    y is a function of x.
    """
    dydx2 = np.zeros(y.shape,float)
    dydx2[1:-1] = (y[2:]-y[:-2])/(x[2:]-x[:-2]) #Code for middle points
    dydx2[0] = (y[1]-y[0])/(x[1]-x[0]) #First Point
    dydx2[-1] = (y[-1]-y[-2])/(x[-1]-x[-2])#Final Point
    return dydx2
    
 