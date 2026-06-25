def b(n):
    return(bin(n)[2:])
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

    
    