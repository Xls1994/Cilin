# -*- coding:utf-8 *-*
def cMax(x,y):
    z =max(x,y)
    return z
def cMin(x,y):
    z =min(x,y)
    return z
def cPelace1(x,y):
    if x==1.0:
        z =y
    else :
        z =x
    return z
def ariMean(x,y):
    z = (x + y)/2
    return  z
def geoMean(x,y):
    import math
    z =math.sqrt(x*y)
    return  z
if __name__=='__main__':
    print 'hello world.'
    z =geoMean(3,6)
    print z