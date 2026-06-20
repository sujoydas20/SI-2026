def merge(l1,l2):
  x1 = len(l1)
  x2 = len(l2)
  x = x1 + x2
  l = [0]*(x)
  for i in range(x):
    if i%2 == 0:
      try:
        if l1[i//2] == 1:
          l[i] = 1
      except IndexError:
        if l2[i//2] == 1:
          l[i] = 1
    else:
      try:
        if l2[i//2] == 1:
          l[i] = 1
      except IndexError:
        if l1[i//2] == 1:
          l[i] = 1
  return(l)

def cis(x,y):
  l = [0]*x
  for i in range(y):
    l[i] = 1
  c1 = []
  z = x - y
  for i in range(z):
    l1 = l[:]
    l1[y-1] = 0;l1[y+i] = 1
    c1.append(l1)
  return c1

def cisd(x,y):
  l = [0]*x
  for i in range(y):
    l[i] = 1
  c2 = []
  c1 = cis(x,y)
  z = y - 1
  for i in c1:
    k = z
    while(i[k] == 0):
      l2 = i[:]
      l2[z-1] = 0;l2[k] = 1
      c2.append(l2)
      k += 1
  return c2

def cisdt(x,y):
  l = [0]*x
  for i in range(y):
    l[i] = 1
  c3 = []
  c2 = cisd(x,y)
  z = y - 1
  for i in c2:
    k = z - 1
    while(i[k]==0):
      l3 = i[:]
      l3[z-2] = 0;l3[k] = 1
      c3.append(l3)
      k += 1
  return c3
    
def per(x,y):

  if y < 0 or y > x:
    return []

  if x == 0:
    return [[]]

  if x == 1:
    if y == 0:
      return [[0]]
    elif y == 1:
      return [[1]]
    else:
      return []

  if y == 0:
    return [[0]*x]

  if x == y:
    return [[1]*x]

  c = []

  for i in range(y+1):

    a = per(x//2, i)
    b = per(x - x//2, y-i)

    for p in a:
      for q in b:
        c.append(p+q)

  return c

def plus(l1,l2):
  c = []
  def ino(l):
    if not isinstance(l, list):
        return False

    for x in l:
        if isinstance(x, list):
            for y in x:
                if isinstance(y, list):
                    return False
            return True

    return False
  if(ino(l1) and ino(l2)):
    for i in l1:
      for j in l2:
        c.append(merge(i,j))
    return(c)
  elif(ino(l1) or ino(l2)):
    if(ino(l1)):
      for i in l1:
        c.append(merge(i,l2))
      return(c)
    else:
      for i in l2:
        c.append(merge(l1,i))
      return(c)
  else:
    c.append(merge(l1,l2))
    return(c)

def gr(x,y):
  l = [0]*x
  for i in range(y):
    l[i] = 1
  return l

x = input("level of theory(CIS,CISD,CISDT,FCI):")
a =int(input("enter the number of spin up orbitals:"))
b = int(input("input the number of spin up electrons:"))
c = int(input("input the number of spin down orbitals:"))
d = int(input("input the number of spin down electrons:"))
  
def call(x,a,b,c,d):
  match x:
    case "CIS":
      g = []
      g.append(plus(cis(a,b),gr(c,d)))
      g.append(plus(gr(a,b),cis(c,d)))
    case "CISD":
      g = []
      g.append(plus(cis(a,b),gr(c,d)))
      g.append(plus(gr(a,b),cis(c,d)))
      g.append(plus(cisd(a,b),gr(c,d)))
      g.append(plus(gr(a,b),cisd(c,d)))
      g.append(plus(cis(a,b),cis(c,d)))
    case "CISDT":
      g = []
      g.append(plus(cis(a,b),gr(c,d)))
      g.append(plus(gr(a,b),cis(c,d)))
      g.append(plus(cisd(a,b),gr(c,d)))
      g.append(plus(gr(a,b),cisd(c,d)))
      g.append(plus(cis(a,b),cis(c,d)))
      g.append(plus(cisdt(a,b),gr(c,d)))
      g.append(plus(gr(a,b),cisdt(c,d)))
      g.append(plus(cisd(a,b),cis(c,d)))
      g.append(plus(cis(a,b),cisd(c,d)))
    case "FCI":
      g = []
      g.append(plus(per(a,b),per(c,d)))
    case _:
      print("invalid Input choose from(CIS,CISD,CISDT,FCI)")
  return g

g = call(x,a,b,c,d)[0]
print(g)
print(len(g))


