class nodes
{
  float a,b;
  float size = 5;
  nodes(float x,float y)
  {
    a = x; b = y;
    ellipse(a,b,size, size);
  }
  
  float getX()
  {
    return a;
  }
  
  float getY()
  {
    return b;
  }
}


float d(nodes x, nodes y)
{
  float dis = sqrt((x.getX() - y.getX())*(x.getX() - y.getX()) + (x.getY() - y.getY())*(x.getY() - y.getY()));
  return dis;
}


int size = 700;
nodes[] X = new nodes[size];
void setup()
{
  size(800, 800);
  background(0);
  fill(255);
 for(int i = 0 ; i < size ; i++)
 {
   float x = random(0,800);
   float y = random(0, 800);
   X[i] = new nodes(x,y);
 }
}

void draw()
{
  for(int j = 0 ;j < size; j++)
  {
 
  for( int k = 0 ; k < size; k++)
  {
    if(j == k)
    continue;
    strokeWeight(1);
    stroke(0,51,70);
    if(d(X[j], X[k]) < 40)
    {
      line(X[j].getX(), X[j].getY(), X[k].getX(), X[k].getY());
    }
  }
  }
  
  
}
