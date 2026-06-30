from math import comb
import numpy as np
import Basis_operations.basis as bi

n = 0 #number of spin orbitals
k = 0 #number of electrons
c = 0 #dimension of occupation number space
m = 0 #number of sites or atoms
per = False #cyclic system or not
x_huc = 0

b = 1 #hopping parameter
u = 1 #intrasite repulsion parameter

rij = 1.40 #Bond length
r = np.zeros((m,m)) #Distance matrix

ba = []
    
def hu():
    global m,x_huc
    m = int(input("enter the number of atoms"))
    x_huc = input("""linear open chain system(0)
    monocylic(1)
    neither(2)""")

def hr():
    global n,k,c,m
    n = int(input("enter the number of spin orbitals:"))
    k = int(input("enter the number of electrons"))
    c = comb(n,k)
    m = n//2
    global b,u,ba
    b = float(input("enter the value of hopping parameter:"))
    u = float(input("enter the value of intrasite repulsion parameter:"))
    ba = bi.binary_hash(bi.per(n,k))
def ehr():
    global n,k,c,m
    n = int(input("enter the number of spin orbitals:"))
    k = int(input("enter the number of electrons"))
    c = comb(n,k)
    m = n//2
    global b,u,rij,e_r,ba
    b = float(input("enter the value of hopping parameter:"))
    u = float(input("enter the value of intrasite repulsion parameter:"))
    rij = float(input("enter the bond length"))
    ba = bi.binary_hash(bi.per(n,k))
def p():
    global n,k,c,m
    n = int(input("enter the number of spin orbitals:"))
    k = int(input("enter the number of electrons"))
    c = comb(n,k)
    m = n//2
    global b,u,r,e_r,ba
    b = float(input("enter the value of hopping parameter:"))
    u = float(input("enter the value of intrasite repulsion parameter:"))
    for i in range(m):
        for j in range(m):
            r[i][j] = float(input(f"input the {i+1}{j+1}th value of the distance matrix: "))
    ba = bi.binary_hash(bi.per(n,k))

