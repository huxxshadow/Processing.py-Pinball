



class Button():
    global o
    o=0
    
    def __init__(self,i,xP,yP,le,he,f1,t,v,s,ty,c,ts):
        self.x=xP
        self.y=yP
        self.h=he
        self.l=le
        self.font11 = f1
        self.content=t
        self.index =i
        self.addL=0
        self.addH=0
        self.sound=s
        self.volume=v
        self.type=ty
        self.colour=c
        self.textsize=ts

        
    def show(self):
        #two types buttons
        if self.type==1:
            pushMatrix()
            rectMode(CENTER)
            strokeCap(ROUND)
            stroke(self.colour)
            strokeWeight(8)
            fill(149,193,148)
            rect(self.x,self.y,self.l+self.addL,self.h+self.addH,80)
            rectMode(CORNER)
            fill(self.colour)
            textFont(self.font11)
            textAlign(CENTER,CENTER)
            text(self.content,self.x,self.y-20)
            noStroke()
            popMatrix()
        elif self.type==2:
            pushMatrix()
            rectMode(CENTER)
            strokeCap(ROUND)
            stroke(self.colour)
            strokeWeight(8)
            noFill()
            ellipse(self.x,self.y,self.l+self.addL,self.h+self.addH)
            rectMode(CORNER)
            textFont(self.font11)
            textAlign(CENTER,CENTER)
            textSize(self.textsize)
            text(self.content,self.x,self.y-self.textsize/4)
            strokeWeight(0)
            noStroke()
            popMatrix()
            
    def ifMouseOver(self):
        #if Mouse Over the button,button size will increase
        if self.type==1:
            if mouseX<=self.x+self.l/2 and mouseX>=self.x-self.l/2 and mouseY<=self.y+self.h/2 and mouseY>=self.y-self.h/2:
                self.addL=constrain(self.addL+5,0,250)
                self.addH=constrain(self.addH+2,0,100)
                # if Mouse click the button it will play music effect
                # due to the bug of sound library you should through the processing to close the process,otherwise the sound has no volume
                if mousePressed:
                    self.sound.amp(self.volume)
                    self.sound.play()
                    return self.index
            else:
                self.addL=constrain(self.addL-5,0,240)
                self.addH=constrain(self.addH-3,0,100)
                
        elif self.type==2:
            if dist(mouseX,mouseY,self.x,self.y)<=self.h:
                if mousePressed:
                    global o
                    o+=1
                    if o==6:
                        o=0
                        # print("a")
                        self.sound.amp(self.volume)
                        self.sound.play()
                        return self.index
            
        
        
        
        
        
    
