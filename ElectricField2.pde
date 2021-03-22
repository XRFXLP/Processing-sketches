void setup()
{
  size(800,800);
}
PVector A,B,C,D;
PVector[] v = new PVector[400];
PVector M;
float c;
void draw()
{
  translate(400,400);
  background(255);
  M = new PVector(mouseX - 400, mouseY - 400);
  fill(255,255,0,100);
  ellipse(M.x, M.y , 10,10);
  for(int i = -10;i < 10; i++)
  {
    for(int j = -10; j< 10;j++)
    {
      int e = 20*(i + 10) + (j + 10);
      v[e] = new PVector(20+ j*40, 20+ i*40);
      B = new PVector(M.x - v[e].x , M.y - v[e].y);
      B.normalize().mult(10);
      line(v[e].x, v[e].y, v[e].x + B.x, v[e].y + B.y);
    }
  }
}
