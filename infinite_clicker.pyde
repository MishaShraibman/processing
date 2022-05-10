x = 1
b = 0
y = 8
def setup():
    size(600,400)
    
def draw():
    global x,b,y
    background(255)
    translate(300,200)
    ellipseMode(CENTER)
    fill(0)
    ellipse(0,0,100,100)
    textSize(25)
    text(b,150,175)
    if b >= y:
       rectMode(CENTER)
       fill(255)
       rect(200,-100,100,70)
       if mousePressed == True:
          if mouseX > 450 and mouseX < 550 and mouseY < 135 and mouseY > 65:
             y = y * 3
             x = x * 2
             b = 0
    
def mouseClicked():
    global x,b,y
    xDif = 300 - mouseX
    yDif = 200 - mouseY
    if sqrt(xDif*xDif + yDif*yDif) < 35:
        b = b+x
