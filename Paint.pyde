def setup():
    size(600, 600)
    background(255)
    
    fill(0)
    rect (120,120, 400, 400)
    fill(255)
    rect (177,180, 343, 270)
    fill(225,200,0)
    rect (130,140, 20, 20)
    fill(0,255,0)
    rect (130,161, 20, 20)
    fill(0,0,255)
    rect (130,182, 20, 20)
    fill(255,0,0)
    rect (130,201, 20, 20)
    fill(154,50,205)
    rect (130,222, 20, 20)
    fill(random(255), random(255), random(255))
    rect (130,243, 20, 20)
    
    
 
def draw():
    if mousePressed and (mouseX>180 and mouseX<=515) and (mouseY>200 and mouseY<450):
        line(pmouseX, pmouseY, mouseX, mouseY)
    if mousePressed and (mouseX<=180 and mouseX>110) and (mouseY>140 and mouseY<=160):
        stroke(225,200,0)
    if mousePressed and (mouseX<=180 and mouseX>110) and (mouseY>160 and mouseY<=180):
        stroke(0,255,0)
    if mousePressed and (mouseX<=180 and mouseX>110) and (mouseY>180 and mouseY<=195):
        stroke(0,0,255)
    if mousePressed and (mouseX<=180 and mouseX>110) and (mouseY>195 and mouseY<=215):
        stroke(255,0,0)
    if mousePressed and (mouseX<=180 and mouseX>110) and (mouseY>215 and mouseY<=235):
        stroke(154,50,205)
    if mousePressed and (mouseX<=180 and mouseX>110) and (mouseY>235 and mouseY<=255):
        line(pmouseX, pmouseY, mouseX, mouseY)
        stroke(random(255), random(255), random(255))
        
