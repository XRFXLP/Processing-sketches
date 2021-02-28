from random import randint
M = set()
def setup():
    size(1300, 700)
    background(255)
    translate(width/2, height/2)
    strokeWeight(2)
    for i in range(-300, 300, 60):
        for j in range(-300, 300, 60):
            k = randint(0, 2) * 255
            fill(k)
            if k == 0:
                M.add((i, j))
            rect(i, j, 60, 60)

def draw():
    global M
    translate(width/2, height/2)
    x, y = mouseX - width/2, mouseY - height/2
    if -300 <= x < 300 and -300 <= y < 300:
        fill(24, 60, 100)
        xs, ys = (x + 300) // 60, (y + 300) // 60
        p, q = 60 * xs - 300, 60 * ys - 300
        if (p, q) not in M:
            rect(p,q, 60, 60)
        
