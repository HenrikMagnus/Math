import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

fig, ax = plt.subplots(figsize=(8,8))
plt.title(r'$y_{1}=ax+b, \ y_{2}=cx+d$')
plt.xlabel('x')
plt.ylabel('y',rotation=True)
plt.subplots_adjust(left=0.12, bottom=0.26)
plt.xlim(-10,10)
plt.ylim(-10,10)
plt.xticks(np.arange(-10,11,1))
plt.yticks(np.arange(-10,11,1))
x = np.arange(-10,10,0.001)
#1. Funktion
def f1(x,a=1,b=1):
    return a*x+b
#2. Funktion
def f2(x,c=-1,d=5):
    return c*x+d
#Initialisierung
y1,y2 = plt.plot(x,f1(x,1,1),x,f2(x,-1,5),lw=1.5)
#x-, y-Position, Laenge, Hoehe
xyA = plt.axes([0.1, 0.15,0.8,0.03])
xyB = plt.axes([0.1, 0.1,0.8,0.03])
xyC = plt.axes([0.1, 0.05,0.8,0.03])
xyD = plt.axes([0.1, 0.00,0.8,0.03])
#Slider erzeugen
sldA = Slider(xyA,'a',-5.0,5.0,valinit=1,valstep=0.1)
sldB = Slider(xyB,'b',-10.0,10.0,valinit=1,valstep=0.1)
sldC = Slider(xyC,'c',-5.0,5.0,valinit=-1,valstep=0.1)
sldD = Slider(xyD,'d',-10.0,10.0,valinit=5,valstep=0.1)
#neue Position berechnen
def update(val):
    a = sldA.val
    b = sldB.val
    c = sldC.val
    d = sldD.val
    y1.set_data(x,f1(x,a,b))
    y2.set_data(x,f2(x,c,d))
    fig.canvas.draw_idle()
#Änderung abfragen
sldA.on_changed(update)
sldB.on_changed(update)
sldC.on_changed(update)
sldD.on_changed(update)
ax.grid(True)
plt.show()