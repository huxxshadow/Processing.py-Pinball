
from button import Button
from interface import Interface

class EndInterface(Interface):
    global x,y,yIn,x2,y2
    x=0
    y=0
    x2=0
    y2=0
    yIn=0
    
    
    def __init__(self,fonts,sounds,v,i1,s):
        Interface.__init__(self,fonts,sounds,v)
        
        self.song= s
        self.s2=s
        self.num=0
        self.rotateN =0
        self.dist1=1200
        self.dist2=1200
        self.rad1=-20
        self.rad2=-300
        self.eList=[0]
        self.greenC=255
        self.button1= Button(1,170,170,100,100,self.font5,"R",self.volume,self.sound1,2,color(128,209,200,20),50)
        self.button2= Button(2,-170,-170,100,100,self.font5,"E",self.volume,self.sound1,2,color(128,209,200,20),50)
        # print((self.volume-1)*100)
        # self.song.setGain((self.volume-1)*100)
        self.n=0
        
    def working(self):
        #minim song control
        if self.song.getGain!=self.volume:
            if self.volume<0.1:
                self.song.setGain(-80)
            else:
                self.song.setGain((self.volume-1)*15)
            # print(self.song.getGain())
        if self.song.isPlaying()==0:
            self.song.loop()
        
        self.show()
        self.buttonsShow()
        q=self.buttonsDete()
        if q!=None:
            self.n+=1
            if self.n>=2:
                self.n=0
                self.song.pause()
                return q
        
    def buttonsShow(self):
        self.button1= Button(1,1000+cos(self.rotateN)*170,900+sin(self.rotateN)*170,100,100,self.font5,"R",self.volume,self.sound1,2,color(128,209,200,20),50)
        self.button2= Button(2,1000+cos(self.rotateN)*-170,900+sin(self.rotateN)*-170,100,100,self.font5,"E",self.volume,self.sound1,2,color(128,209,200,20),50)
        self.button1.show()
        self.button2.show()

        
    def buttonsDete(self):
        j=self.button1.ifMouseOver()
        k=self.button2.ifMouseOver()
        if j != None:
            # print(j)
            return j
        elif k!=None:
            
            exit()
        
        
        
    def show(self):
        noStroke()
        fill(2,2,26,10)
        rect(0, 0, width, height)
        if self.song.mix.level()*100>18:
            if self.song.mix.level()*100>15:
                # print(self.num)
                self.num+=1
                if self.num==40:
                    self.num=0
                if len(self.eList)==20:
                    if self.num>=20:
                        self.eList.remove(self.num-20)
                        # print(self.num)
                    if self.num<20:
                        self.eList.remove(self.num+20)
                        # print(self.num)    
                
                self.eList.append(self.num)
            self.greenC=constrain(self.greenC-3,155,255)
        else:
            self.greenC=constrain(self.greenC+1,155,255)
        fill(random(0, 5),self.greenC, 255,90)
        self.rotateN +=self.song.mix.level()*0.05
        pushMatrix()
        translate(width/2,height/2)
        rotate(self.rotateN)
        
        # rect(0,0,500,500)
        rate=0
        #when number < bufferSize() isn't vaild
        while(rate <=360):
            for i in range(self.song.bufferSize()):
                global x,y,yIn,x2,y2
                rate+=1
                angle = radians(rate)
                x= cos(i)*(self.rad1+ ((self.dist1)* noise(y/50, yIn)))
                y= sin(i) * (self.rad1 + ((self.dist1+self.song.mix.level()*30) * noise(x/480, yIn)))        
                ellipse(x*1, y*1, 2, 2);
                x2 = sin(i) * (self.rad2 + (self.dist2 * noise(y2/(0.01+self.song.mix.level()*20), yIn)))
                y2= cos(i) * (self.rad2 + (self.dist2 * noise(y2/(0.01+self.song.mix.level()*20), yIn)))
                ellipse(x2*2, y2*2, 1.2, 1.2);
                # if self.song.mix.get(i)*100>35:
                #     # self.eList.append()
                #     print(self.song.mix.get(i))
                # ellipse(90,90,self.song.mix.get(i)*30,self.song.mix.get(i)*30)
                # ellipse(20,-0.01,self.song.mix.get(i)*30,self.song.mix.get(i)*30)
                # ellipse(10,-100,self.song.mix.get(i)*30,self.song.mix.get(i)*30)    
                
            for j in self.eList:
                ellipse((90+20*j)*cos(TWO_PI/15*j),(90+20*j)*sin(TWO_PI/15*j),self.song.mix.get(i)*50,self.song.mix.get(i)*50)
                # ellipse((-90-20*j)*cos(TWO_PI/15*j),(90+20*j)*sin(TWO_PI/15*j),self.song.mix.get(i)*50,self.song.mix.get(i)*50)
                ellipse((-90-20*j)*cos(TWO_PI/15*j),(-90-20*j)*sin(TWO_PI/15*j),self.song.mix.get(i)*50,self.song.mix.get(i)*50)
            
            fill(random(0, 5),self.greenC,255,20)
            # ellipse(170,170,100,100)

        self.buttonsDete()
        yIn += 0.003
        
        
        popMatrix()
        # return c
        
        
        
