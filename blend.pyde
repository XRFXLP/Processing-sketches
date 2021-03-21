'''
This little script loads two images from memory and blend them 
'''
def co(Q):
    return red(Q), green(Q), blue(Q)
def norma(a,b):
    return [i*0.5 + j*0.3 for i, j in zip(a,b)]
def setup():
    C = loadImage("CB.jpg")
    J = loadImage("JD.jpg")
    
    J.resize(244, 318)
    J.resize(244 * 2, 318 * 2)
    C.resize(488, 636)
    background(255)
    size(488, 636)
    for i in range(0, 488, 2):
        for j in range(0, 636, 2):
            c1 = co(C.get(i, j - 43))
            c2 = co(J.get(i, j))
            fill(*norma(c1, c2))
            ellipse(i, j, 2, 2)
