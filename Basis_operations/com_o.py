import com

def ca(y,x,l):
    k = set(l)
    if x not in k:
        return 0, None
    if y in k:
        return 0, None
    def a(x,l):
        g = 0
        for i in range(1,len(l)+1):
            if l[-i] == x:
                del l[-i]
                break
            g += 1
        return g,l
    def c(y,l):
        h = 0
        for i in range(1,len(l)+1):
            if i == len(l):
                l.insert(-i,y)
            elif l[-i-1] > y:
                l.insert(-i,y)
                break
            h += 1
        return h,l
    
    g,l1 = a(x,l)
    h,l2 = c(y,l1)

    return (g+h)%2,l2

x,l = ca(4,2,[3,2,0])

print(x)
print(l)