import config as con
import Basis_operations.basis as ba
import Basis_operations.binary as bi
import numpy as np

def dp(v1,v2): #it is expected that v1 is a hash of a vector and v2 is [n,# of vector] where n is a integer
    if v1 == v2[1]:
        return v2[0]
    else:    
        return 0

def exp(fun,evec): #this function give the expectation value of operator(fun()) on # of vector evec
    k = 0
    for i in evec:
        for j in evec:
            k += dp(i,fun(j))
    return k

def double_occ(evec):
    k = 0
    for i in range(con.m):
        if bi.nus(2*i,evec) == 2:
            k += 1
    return k

def expval(f,vec):
    k = 0
    ba = con.ba
    l = len(vec)
    for i in range(l):
        k += (np.linalg.norm(vec[i])**2)*(f(ba[i]))
    return k





