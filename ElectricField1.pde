ArrayList <PVector> W = new ArrayList <PVector> ();
void setup()
{
  size(800,800);
  frameRate(300);
}
PVector B;
int count = 0;
int fv = 900;
PVector[] v = new PVector[fv];
PVector M;
float c;
void draw()
{
  stroke(255);
  translate(400,400);
  background(0);
  M = new PVector(mouseX - 400, mouseY - 400);
  for(int i = -(int)sqrt(fv)/2; i < (int)sqrt(fv)/2; i++)
  {
    for(int j = -(int)sqrt(fv)/2; j<(int) sqrt(fv)/2;j++)
    { 
      int e = (int)sqrt(fv)*(i + (int)sqrt(fv)/2 ) + (j + (int)sqrt(fv)/2);
      v[e] = new PVector(sqrt(fv)/2 + j*800/sqrt(fv), 20+ i*800/sqrt(fv));
      B = new PVector(M.x - v[e].x , M.y - v[e].y);
      
      if(W.size() != 0)
      {
        for(int k =0; k < W.size(); k++)
        {
          if(W.get(k).x > 0)
          {
          PVector L;
          L = new PVector(W.get(k).x - v[e].x, W.get(k).y - v[e].y);
          L.mult( 9*pow(10,9)/ pow(L.mag(),3));
          B.add(L);
          }
           if(W.get(k).x < 0)
          {
            PVector L;
            L = new PVector(-W.get(k).x + v[e].x, -W.get(k).y + v[e].y);
            L.mult( 9*pow(10,9)/ pow(L.mag(),3));
            B.add(L);
            
          }
         }
      }
      stroke(B.mag()/100,0,255);
      B.normalize().mult(20);
      line(v[e].x, v[e].y, v[e].x + B.x, v[e].y + B.y);
      }
   }
   
   for(int i =0 ;i<W.size();i++)
   {
     if(W.get(i).x > 0)
     fill(0,0,255);
     noStroke();
     ellipse(W.get(i).x, W.get(i).y , 10,10);
     if(W.get(i).x < 0)
     {
       fill(255,0,0);
       ellipse(W.get(i).x, W.get(i).y , 10,10);
     }
   }
}
void mousePressed()
{
        fill(0); 
        W.add(new PVector(mouseX - 400, mouseY - 400));
}
