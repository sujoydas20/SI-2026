from math import comb
import numpy as np

n = 0 #number of spin orbitals
k = 0 #number of electrons
c = 0 #dimension of occupation number space
m = 0 #number of sites or atoms
per = False #cyclic system or not
x_huc = 0

a = 1 #onsite energy
b = 1 #hopping parameter
u = 1 #intrasite repulsion parameter

global e_r,rij,r
e_r = 8.854e-12
rij = 1.40e-10
r = np.zeros((m,m))

def ini1():
    global n,k,c,m,per

    n = int(input("input the number of spin orbitals"))
    k = int(input("enter the number of electrons"))
    per = input("is the system open or closed(0/1):")
    
    c = comb(n,k)

    m = n//2

def ini3():
    for i in range(m):
        for j in range(m):
            r[i][j] = float(input(f"input the {i}{j}th value of the matrix: "))

def hu():
    global n,x_huc
    n = int(input("enter the number of atoms"))
    x_huc = input("""linear open chain system(0)
                     monocylic(1)
                     neither(2)""")
    global a,b
    a = float(input("Enter the value of onsite energy"))
    b = float(input("Enter the value of hopping parameter"))

def hr():
    global n,k,c,m
    n = int(input("enter the number of spin orbitals:"))
    k = int(input("enter the number of electrons"))
    c = comb(n,k)
    m = n//2
    global b,u
    b = float(input("enter the value of hopping parameter:"))
    u = float(input("enter the value of intrasite repulsion parameter:"))


