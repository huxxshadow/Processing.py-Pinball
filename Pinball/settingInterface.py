from interface import Interface
from button import Button

class SettingInterface(Interface):
    global colors,rains
    colors = [color(117,185,177),color(105, 109, 125),color(215,38,56),color(244, 157, 55),color(20,15,45)]
    rains = list()
    
    
    def __init__(self,fonts,sounds,v,i1):
        
        Interface.__init__(self,fonts,sounds,v)
        self.img1=i1
        self.button1 = Button(0,300,550,200,200,self.font1,"+",self.volume,self.sound1,2,color(128,209,200),225)
        self.button2 = Button(1,600,550,200,200,self.font1,"-",self.volume,self.sound1,2,color(128,209,200),225)
        self.button3 = Button(3,1700,1600,600,200,self.font1,"Back",self.volume,self.sound1,2,color(128,209,200),180)
        
    def working(self):
        self.startBackground()
        self.drawText()
        self.startButtons()
        return self.buttonsDete()
        
    
    def startButtons(self):
        self.button1.show()
        self.button2.show()
        self.button3.show()
    
    def drawText(self):
        pushMatrix()
        textAlign(CENTER,CENTER)
        textFont(self.font1)
        image(self.img1,500,200,200,200)
        textSize(200)
        text("Setting",1100,150)
        fill(0xd0,0xea,0xd6,20)
        rect(1455,445,350,200,60)
        fill(117,185,177,20)
        text("volume",1100,500)
        text(str(int(self.volume*100)),1630,500)    
        popMatrix()
    def buttonsDete(self):
        j=self.button1.ifMouseOver()
        k=self.button2.ifMouseOver()
        l=self.button3.ifMouseOver()
        if j != None:
            if self.volume<1:
                return self.volume+0.1
        elif k!=None:
            if self.volume>=0.1:
                return self.volume-0.1
        elif l!=None:
            return l
    
    def startBackground(self):

        if frameCount%10==0:
            rains.append(drip(colors,random(5,30),random(width),random(-100,height)))
            noStroke()
            fill(color(0xd0,0xea,0xd6,10))
            rect(0,0,width,height)
        j=len(rains)-1
        while j>=0:
            rains[j].move()
            rains[j].show()
            j-=1
    
class drip:
    def __init__(self,cs,p,xp,yp):
        self.colour= cs[int(random(len(cs)))]
        self.splats =list()
        self.x=xp
        self.y=yp
        self.death=300
        self.extent=random(20,80)
        self.noiseStart=random(TWO_PI)
        i=self.noiseStart
        while i<self.noiseStart+TWO_PI:
            ad = noise(i)
            self.splats.append(pointer(i,ad,self.extent))
            i+=random(0.2)
            
    def move(self):
        for n in self.splats:
            n.move()
        self.death-=1
        if self.death<1:
            del rains[rains.index(self)]
    
    def show(self):
        noStroke()
        s= hex(self.colour,6)
        r= int(s[0:2],16)
        g= int(s[2:4],16)
        b= int(s[4:6],16)
        
        ne =color(r,g,b,80)
        fill(ne)
        push()
        translate(self.x,self.y)
        beginShape()
        for spl in self.splats:    
            # curveVertex(spl.pos.x,spl.pos.y)
            ellipse(spl.pos.x,spl.pos.y,random(12),random(12))
        endShape(CLOSE)
        pop()

        
class pointer:
    def __init__(self,o,n,fSize):
        self.rad=o
        self.distance=1
        self.no=n
        self.speed=0
        self.pos = PVector(0,0)
        self.finalSize=fSize
        self.downSpeed= PVector(0,0.01)
        self.downNo= PVector(0,0.1+self.no/500)        
                            
    def move(self):
        if self.distance<=self.finalSize:
            self.speed+=self.no
            self.distance+=self.speed/2
            self.pos = PVector(cos(self.rad)*self.distance,sin(self.rad)*self.distance)
        else:
            self.downSpeed.add(self.downNo)
            self.pos.add(self.downSpeed) 
                                                    
                                                                
                                                                            
                                                                                                    
                    
