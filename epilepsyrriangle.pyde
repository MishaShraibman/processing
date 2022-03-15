x = 0
y = 0
d = 300
r = 200
f = 0
def setup():
  size(1920,1080)
  colorMode(HSB,100,100,100)
  fullScreen()
  frameRate(45)
def draw():
  global x,y,d,r,f
  background(random(0,100),100,100)
  fill(random(0,100),x,f)
  triangle(y,275,250,r,d,275)
  x = x + 0.5
  y = y - 0.25
  d = d + 0.25
  r = r - 0.25
  f = f + 1
