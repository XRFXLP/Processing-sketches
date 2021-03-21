from random import randint
from math import *
inf = 1e10
H = 1200
V = 700
def are_collinear(p1, p2, p3):
    return p1[1] * ( p2[0] - p3[0]) + p2[1] * ( p3[0] - p1[0]) + p3[1] * ( p1[0] - p2[0]) != 0
random_points = [(0,300)]#[(randint(-300,300), randint(-200, 200)) for i in range(30)]
non_collinear = set([(0,0)])
for i in random_points:
    for j in random_points:
        if i == j:
            continue
        if not any(not are_collinear(i, j, k) for k in random_points if k not in [i, j]):
            non_collinear.add(j)
non_collinear = [(0, 0), (-100, 200), (200, 100), (-100, -200)]
ttt = ["(0, 0)", "(-1, 2)", "(2, 1)", "(-1, -2)"]
from cmath import phase
S = lambda x, y: (x[0] - y[0], x[1] - y[1])
PD =lambda x,C,D:min(map(lambda x:x if x>0 else 2*pi+x,[phase(i*complex(*D))-phase(complex(*S(x,C)))for i in [-1,1]]))

def windmill(P):
    co, dR, i, M = (0, 0), (0, 1), 0, 0
    AC =[]
   # AC.append(((0,0), pi/2))
    while M <= 20*pi:
        ne = min(P, key = lambda x: inf if x == co else PD(x, co, dR))
        M, dR, co, i = M + abs(PD(ne, co, dR)), S(co, ne), ne, i + 1
        AC.append((ne, M+pi/2))
    AC.pop()
    return AC

def setup():
    size(H, V)
    background(255)
    translate(H/2, V/2)
    strokeWeight(5)
t = 1.57
AC = windmill(non_collinear)
temp = (0, 0)
counter = 0


    
def draw():
    global t
    global counter
    global temp
    translate(H/2, V/2)
    t += 0.011

    background(5, 5 ,20)
    fill(255,0,0, 0.5)
    
    if AC and t >= AC[0][1]:
        
        temp = (AC[0][0][0], -AC[0][0][1])
        fill(255, 255, 0)
        counter += 1
        ellipse(temp[0], temp[1], 30, 30)
        AC.pop(0)

    ellipse(temp[0], temp[1], 14, 14)
    
    
    strokeWeight(5)
    for i, j in zip(non_collinear ,ttt):
        fill(249, 250, 250)
        stroke(249, 250, 250)
        point(i[0], -i[1])
        textSize(15)
        text(j, i[0] + 10, -i[1])
    strokeWeight(2.3)
    
    stroke(100)
    
    #line(0 - temp[0], -V/2 - temp[1], 0 - temp[0], V/2 - temp[1])
   # line(-H/2 - temp[0],0 - temp[1],H/2 - temp[0],0 - temp[1])

    
    stroke(77, 78, 127)
    line(temp[0],temp[1], temp[0] + 1400*cos(t), temp[1] + 1400*sin(t))
    line(-1400*cos(t) + temp[0], -1400*sin(t) + temp[1], temp[0],temp[1])
    noStroke()
    fill(255, 81, 5)
    ellipse(temp[0], temp[1], 14, 14)
    
    text("Counter : {}".format(counter), 300, 100)
