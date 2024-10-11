# Extracted from https://stackoverflow.com/questions/12444716/how-do-i-set-the-figure-title-and-axes-labels-font-size
 from numpy import*
 import matplotlib.pyplot as plt
 X = linspace(-pi, pi, 1000)

class Crtaj:

    def nacrtaj(self,x,y):
         self.x=x
         self.y=y
         return plt.plot (x,y,"om")

def oznaci(self):
    return plt.xlabel("x-os"), plt.ylabel("y-os"), plt.grid(b=True)

from numpy import*
M = array([[3,2,3],[1,2,6]])
class AriSred(object):
    def __init__(self,m):
    self.m=m
    
def srednja(self):
    redovi = len(M)
    stupci = len (M[0])
    lista=[]
    a=0
    suma=0
    while a<stupci:
        for i in range (0,redovi):
            suma=suma+ M[i,a]
        lista.append(suma)
        a=a+1
        suma=0
    b=array(lista) 
    b=b/redovi
    return b



OBJ = AriSred(M)
sr = OBJ.srednja()

