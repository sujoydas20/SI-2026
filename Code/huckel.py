import math
import cmath
import numpy as np
import matplotlib.pyplot as plt

def fun(N,x):
  if x == "o":
    eval = []
    for i in range(N):
      eval.append(2*math.cos((i+1)*math.pi*(1.0/(N+1))))
    evec = []
    l = []
    for i in range(N):
      for j in range(N):
        l.append((math.sqrt(2*(1.0/(N+1))))*math.sin((j+1)*(i+1)*math.pi*(1.0/(N+1))))
      evec.append(l)
      l = []
    return eval,evec
  elif x == "c":
    eval = []
    for i in range(N):
      eval.append(math.cos(2*(i)*math.pi*(1.0/N)))
    evec = []
    l = []
    for i in range(N):
      for k in range(N):
        l.append(cmath.exp(2*math.pi*1j*i*(k+1)))
      evec.append(l)
      l = []
    return eval,evec
  else :
     raise ValueError("enter either o or c")

n = int(input("enter the number of carbon atoms:"))
x = input("is the system open or closed(o/c):")
eval,evec = fun(n,x)
print(eval)
print(evec)

def plot_spectrum(eigenvalues, tol=1e-6):

    eig = np.sort(eigenvalues)

    fig, ax = plt.subplots(figsize=(5,6))

    i = 0
    while i < len(eig):

        lam = eig[i]
        deg = 1

        while i + deg < len(eig) and abs(eig[i+deg] - lam) < tol:
            deg += 1

        # Hückel energy ordering (β < 0)
        y = -lam

        xs = np.linspace(-0.3, 0.3, deg)

        for x in xs:
            ax.plot([x-0.12, x+0.12], [y, y], 'k', lw=3)

        # Labels in α + λβ form
        if abs(lam) < tol:
            label = r'$\alpha$'
        elif lam > 0:
            if abs(lam - 1) < tol:
                label = r'$\alpha + \beta$'
            else:
                label = rf'$\alpha + {lam:g}\beta$'
        else:
            if abs(lam + 1) < tol:
                label = r'$\alpha - \beta$'
            else:
                label = rf'$\alpha - {abs(lam):g}\beta$'

        ax.text(0.6, y, label, va='center', fontsize=12)

        i += deg

    ax.set_xlim(-0.8, 1.8)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_title("Hückel Spectrum")

    for spine in ax.spines.values():
        spine.set_visible(False)

    plt.tight_layout()
    plt.show()

plot_spectrum(eval)

