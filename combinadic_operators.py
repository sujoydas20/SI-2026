import combinadic
def ani(n,l):
    k = 0
    for i in range(len(l)):
        if l[i] == n:
            l.remove(n)
            break
        k += 1
    if k%2 == 1:
        l.insert(0,0)
    return l