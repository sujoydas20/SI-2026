import config as con
import math
import Basis_operations.binary as bi
import Basis_operations.basis as basis
import numpy as np
from . import hubbard as hub

ohno = math.sqrt(1+(con.u*con.rij/14.397)**2)
m_n = 1 + (con.u*con.rij/14.397)

def ext(l):
    k1 = 0
    pairs = [(2*i, 2*i+2) for i in range(con.m-1)]
    if con.per:
        pairs.append((2*con.m-2, 0))
    for i,j in pairs:
        k1 += (con.u/ohno)*(bi.nus(i,l)-1)*(bi.nus(j,l)-1)
    return k1

def main_ext():
    bas = con.ba
    mat1 = np.zeros((con.c, con.c))
    for i in range(con.c):
        for j in range(i, con.c):
            if i == j:
                mat1[i][j] = hub.hub(bas[j])*con.u + ext(bas[j])
            else:
                hop = hub.hopp(bas[j])
                if hop is not None:
                    val = hub.dp(bas[i], hop)*con.b
                    mat1[i][j] = val
                    mat1[j][i] = val
    return mat1


