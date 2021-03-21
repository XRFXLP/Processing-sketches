from time import sleep
def setup():
    size(600, 600)
    background(255)
dic = {37: 'L', 38:'U', 39: 'R', 40: 'D'}
H, V = 0, 0
class B:
    def __init__(self, loc, value, L):
        self.loc = loc
        self.value = value
        self.L = L
    def show(self):
        noFill() if self.value else fill(0)
        rect(self.loc[0], self.loc[1], self.L, self.L)
        fill(0)
        text(self.value, self.loc[0] + self.L//2, self.loc[1] + self.L//2)
        
add = lambda x, y: (x[0] + y[0], x[1] + y[1])
mul = lambda s, v: (s * v[0] , s * v[1])
sub = lambda x, y: (x[0] - y[0], x[1] - y[1])
class grid:
    def __init__(self, mat, loc, box_size, di):
        self.mat = [[B(add(loc, mul(box_size, (j, i))), mat[i][j], box_size) for j in range(di)] for i in range(di)]
        self.loc = loc
        self.di = di
        self.empty = next((i, j) for i in range(di) for j in range(di) if mat[i][j] == 0)
        self.MAP = {'U': (-1, 0), 'D' : (1, 0), 'L' : (0, -1), 'R' : (0, 1)}
        self.L = box_size
    def show(self):
        for i in range(self.di):
            for j in range(self.di):
                self.mat[i][j].show()
    def block(self, direction):
        new = add(self.empty, self.MAP[direction])
        if min(new) < 0 or max(new) > self.di - 1:
            return
        oy, ox = self.empty
        temp = self.mat[oy][ox].value
        print(self.empty, "old")
        self.mat[oy][ox].value = self.mat[new[0]][new[1]].value
        self.mat[new[0]][new[1]].value = temp
        self.empty = new
        print(self.empty, "new", self.mat[self.empty[0]][self.empty[1]].value)
        
        
        
        
matrix = [
          [1, 2, 3, 4],
          [2, 1, 14, 6],
          [3, 4, 2, 8],
          [3, 0, 6, 9]
         ]
G = grid(matrix, (-200, -200), 100, 4)
CODES = {37: 'L', 38: 'U', 39: 'R', 40: 'D'}
def draw():
    global H, V, G
    background(255)
    translate(300, 300)
    G.show()
    if keyPressed and key == CODED:
        C = CODES[keyCode]
        sleep(0.5)
        G.block(C)
        print("Yes, lol")
