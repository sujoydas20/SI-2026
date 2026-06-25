from math import comb
from functools import cache

@cache
# this just the choose function with x choose y
def ch(x,y):
    if x < y:
        return 0
    else:
        return comb(x,y) 
# given a index this function gives out the corresponding occupation string 
def com(n,x,y):
    l = []
#vlarge here find out the maximum possible value of v < n such that ch(v,x) < y
    def vlarge(n,x,y):
        if y == 0: 
            return x-1 
        z = 0
        for i in range(n):
            if ch(n-(i+1),x) < y:
                z = n - (i+1)
                break 
        return z
    k = n
    for i in range(y):
        m = vlarge(x,y-i,k)
        l.append(m)
        k = k - ch(m,y-i)
    return l

# this function creates all the possible permutation of given n and k 
def per(x,y):
    z = int(ch(x,y))
    l = []
    for i in range(z):
        l.append(com(i+1,x,y))
    return l

if __name__ == "__main__":
    print(per(5,3))
