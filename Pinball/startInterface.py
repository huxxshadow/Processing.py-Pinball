# add_library('controlP5')

from button import Button
from interface import Interface

class StartInterface(Interface):

    global heightRandom,isLoad,loopNumber,mouseAngle
    heightRandom=0
    isLoad = 0
    loopNumber =0
    mouseAngle=0
    global button1,button2,button3
    
    def __init__(self,fonts,sounds,v,mo,s):
        Interface.__init__(self,fonts,sounds,v)
        self.mouse=mo #image
        self.button1 = Button(2,1000,900,800,200,self.font1,"Start",self.volume,self.sound1,1,color(232,227,223),None)
        self.button2 = Button(3,1000,1200,800,200,self.font1,"Setting",self.volume,self.sound1,1,color(232,227,223),None)
        self.button3 = Button(4,1000,1500,800,200,self.font1,"Exit",self.volume,self.sound1,1,color(232,227,223),None)
        self.song=s
    
    
    
    def working(self):
        if self.song.getGain!=self.volume:
            if self.volume<0.1:
                self.song.setGain(-80)
            else:
                self.song.setGain((self.volume-1)*15)
        if self.song.isPlaying()==0:
            self.song.loop()
        if isLoad == 1:

            self.drawFalseBg()
            self.drawName()
            p=self.drawButton()
            if p!=None:
                # print(p)
                # print("a")
                self.song.pause()
                return p
            
            self.mouseEffect() 
            #loading animation
        elif isLoad ==0:
            self.drawBackground()
    
            
    def drawFalseBg(self):
        noStroke()
        fill(128,209,200)
        rect(0,0,width/2,height)
        noStroke()
        fill(248,245,214)
        rect(width/2,0,width/2,height)

    def drawName(self):
        textAlign(CENTER,CENTER)
        fill(248,245,214)
        textFont(self.font4)
        text("Colourful",500,400)
        textFont(self.font2)
        text("Soli",860,600)
        fill(128,209,200)
        textFont(self.font2)
        text("verie",1130,600)
        textFont(self.font4)
        text("Pinball",1500,400)
                                        
    def drawButton(self):
        
        self.button1.show()
        self.button2.show()
        self.button3.show()
        j=self.button1.ifMouseOver()
        k=self.button2.ifMouseOver()
        l=self.button3.ifMouseOver()
        if j != None:
            return j
        elif k!=None:
            return k
        elif l!= None:
            exit()

        
        
    def mouseEffect(self):
        global mouseAngle
        pushMatrix()
        mouseAngle +=0.1
        translate(mouseX,mouseY)
        rotate(mouseAngle)
        imageMode(CENTER)
        image(self.mouse,0,0)
        range1 = range(1,9)
        range2 = range(1,5)
        for x in range1:
            noFill()
            beginShape()
            stroke(232,227,223)
            strokeWeight(5)
            for y in range2:
                #print(x,y)
                delay(1)
                tx=70*y*sin((TWO_PI/8)*x+random(0.3))
                ty=70*y*cos((TWO_PI/8)*x+random(0.3))
                if mouseX<=width/2:
                    fill(248,245,214)
                else:
                    fill(128,209,200)
                vertex(tx,ty)
            endShape(CLOSE)
        popMatrix()

        
        
    def drawBackground(self):
        global heightRandom,loopNumber,isLoad
        heightRandom= int(constrain(heightRandom+random(100,400),0,height))
        # print(heightRandom)
        loadPixels()
        for x in range(width):
            for y in range(heightRandom):
                tRandom =random(1,11)
                loc =x+y*width
                if x<(width/2):
                    if tRandom <=loopNumber:
                        pixels[loc]=color(128,209,200,100)
                    else:
                        pixels[loc]=color(248,245,214,40)
                else:
                    if tRandom <=loopNumber:
                        pixels[loc]=color(248,245,214,100)
                    else:
                        pixels[loc]=color(128,209,200,30)
        updatePixels()
        textFont(self.font3)
        textAlign(CENTER,CENTER)
        text("Loading...",width/2,height/2)
        loopNumber +=1
        # print(loopNumber)
        if loopNumber >=15:
            isLoad =1
        

    
