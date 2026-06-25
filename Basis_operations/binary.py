""" for a integer n the bin(n) gives "0bxxxx" with the leading 0b represting it is in 
binary format ; b(n) chops of the leading term """
def b(n):
    return(bin(n)[2:])
"""this function toogles the nth bit of a number in its binary representation
;it returns a binary string including the leading terms"""
def tg(l,n):
    x = 2**(n-1)
    y = int(l,2)
    return(bin(y|x))

def gr(x,y):
    l = b(0)
    for i in range(y):
        l = tg(l,x-i)
    return l

x = int(input("enter the number of orbitals"))
y = int(input("enter the number of electrons"))

print(gr(x,y)[2:])
