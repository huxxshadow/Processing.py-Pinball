add_library('jbox2d')
add_library('box2d_processing')

from button import Button
from interface import Interface

from shiffman.box2d import *
from org.jbox2d.dynamics import *
from org.jbox2d.common import *
from org.jbox2d.collision.shapes import *
from org.jbox2d.dynamics.joints import *
from org.jbox2d.dynamics.contacts import *

class GameInterface(Interface):
    
    def __init__(self,fonts,sounds,v,s):
        Interface.__init__(self,fonts,sounds,v)
        self.box2d=Box2DProcessing(this)
        global u,i,o,p,k,t1,t2,t3,c1,c2,c3,c1s,c2s,c3s,life
        u=i=o=p=k=t1=t2=t3=c1=c2=c3=c1s=c2s=c3s=life=0
        self.song= s
        
    def preWorking(self):
        global s5
        self.box2d.createWorld()
        self.box2d.setGravity(0,-50)
        self.score=0
        self.boundary =[]
        self.surface=[]
        self.o1s=[]
        self.circles=[]
        self.particle=[]
        
        self.colors=[0,0,0,0]
        self.colors[0]=[color(248,245,214),color(128,209,200),color(248,245,214),color(128,209,200)]
        self.colors[1]=[color(128,209,200),color(248,245,214),color(128,209,200),color(248,245,214)]
        self.colors[2]=[color(0,49,83),color(229,221,215),color(0,49,83),color(229,221,215)]
        self.colors[3]=[color(229,221,215),color(0,49,83),color(229,221,215),color(0,49,83)]
        self.ink=[list(),list(),list(),list(),list()]
        
        
        self.lv=0
        self.button1=Button(1,100,100,100,100,self.font1,"E",self.volume,self.sound1,2,color(248,245,214),70)
        self.button2=Button(2,100,260,100,100,self.font1,"S",self.volume,self.sound1,2,color(248,245,214),70)
        # self.button3=Button(3,100,420,100,100,self.font1,"P",self.volume,self.sound1,2,color(248,245,214),70)
        s1=[Vec2(200,1400),Vec2(width/2-150,1581),Vec2(width/2-150,1750),Vec2(width/2-50,1800)]
        ss1=Surface(self.box2d,s1,1)
        # s2=[Vec2(width-200,1400),Vec2(width/2+30,height-200)]
        # ss2=Surface(self.box2d,s2,1)
        s2=[Vec2(width-100,200),Vec2(width-200,1400),Vec2(width/2+150,1581),Vec2(width/2+150,1750),Vec2(width/2+50,1800)]
        ss2=Surface(self.box2d,s2,1)
        s3=[Vec2(width-100,200),Vec2(width-70,1700)]
        ss3=Surface(self.box2d,s3,2)
        # s3=[Vec2(width/2-100,1581),Vec2(width/2-30,height-200)]
        # ss3=Surface(self.box2d,s3)
        s4=[Vec2(350,800),Vec2(350,1200),Vec2(835,1400),Vec2(800,800)]
        ss4=Surface(self.box2d,s4,2)
        
        s5=[]
        for x in range(11):
            s5.append(Vec2(350+x*45,800))
        ss5=Surface(self.box2d,s5,2)
        
        s6=[Vec2(1250,800),Vec2(1150,1400),Vec2(1350,1200),Vec2(1250,800)]
        ss6=Surface(self.box2d,s6,2)
        
        
        o11=[Vec2(-33,-10),Vec2(-33,10),Vec2(25,10),Vec2(25,-10)]
        o12=[Vec2(-33,-10),Vec2(-33,10),Vec2(25,10),Vec2(25,-10)]     
             
        self.o1s.append(Object1(self.box2d,width-35,1710,o11,1))
        self.o1s.append(Object1(self.box2d,width-35,1610,o12,1))
        
        self.circles.append(Circle(self.box2d,50,1300,700,self.colors[0][0],1,0))
        self.circles.append(Circle(self.box2d,70,1500,1000,self.colors[1][0],1,0))
        self.circles.append(Circle(self.box2d,40,1400,500,self.colors[2][0],1,0))
        self.circles.append(Circle(self.box2d,55,1600,400,self.colors[3][0],1,0))
        attractor=Circle(self.box2d,20,1610,720,color(255),1,0)
        
        
        # self.boundary.append(RectBoundary(self.box2d,width/2,height/2,1000,10,1))
        self.boundary.append(RectBoundary(self.box2d,width/2,5,width,10,1))
        # self.boundary.append(RectBoundary(self.box2d,width/2,height-5,width,10,1))
        self.boundary.append(RectBoundary(self.box2d,100,height/2,200,height-5,1))
        self.boundary.append(RectBoundary(self.box2d,width-5,height/2,10,height-5,1))
        
        self.surface.append(ss1)
        self.surface.append(ss2)
        self.surface.append(ss3)
        self.surface.append(ss4)
        self.surface.append(ss5)
        self.surface.append(ss6)
        
        self.bounder1=Bounder(self.box2d,ss1,1)
        self.bounder2=Bounder(self.box2d,ss1,2)
        self.rotater=Bounder2(self.box2d)
        self.ball=Ball(self.box2d,30,1600,100,1,color(100),100)
        self.tbs=[Ball(self.box2d,30,500,1000,2,color(c1,c2,c3),100),Ball(self.box2d,30,600,1000,2,color(c1,c2,c3),100),Ball(self.box2d,30,700,1000,2,color(c1,c2,c3),100)]
        self.bpos=None 
        
    def clearAll(self):
        self.ball.clearBody()
            
    def working(self,kl):
        if self.song.getGain!=self.volume:
            if self.volume<0.1:
                self.song.setGain(-80)
            else:
                self.song.setGain((self.volume-1)*15)
        if self.song.isPlaying()==0:
            self.song.loop()
        self.box2d.step()
        self.lv=self.ball.body.getLinearVelocity()
        
        fill(255,255,255,20)
        rectMode(CORNER)
        rect(0,0,width,height)
        self.bounder1.display(kl)
        self.bounder2.display(kl)
        self.rotater.display()
        self.bounder1.toggleMotor()
        self.bounder2.toggleMotor()
        self.rotater.toggleMotor()
        rectMode(CORNERS)
        fill(230,10)
        rect(200,10,width-100,200)
        
        self.drawBridge()
        self.drawColor()
        self.drawAttractor()
        self.drawBall()
        self.drawBoundary()
        
        
        
        
        for i in self.tbs:
            pos=i.display()
            i.force1(Vec2(0,710))
            i.force1(Vec2(random(-10000,10000),random(-10000,10000)))
            pushMatrix()
            translate(pos.x,pos.y) 
            fill(color(c1,c2,c3))
            stroke(0)
            ellipseMode(CENTER)
            ellipse(0,0,i.r*2,i.r*2)
            popMatrix()
        
        fill(229,221,215)
        self.button1.show()
        self.button2.show()
        # self.button3.show()
        
        j=self.button1.ifMouseOver()
        k=self.button2.ifMouseOver()
        # l=self.button3.ifMouseOver()
        
        if j != None:
            self.song.pause()
            return j
            
        elif k!=None:
            self.song.pause()
            return k
        # elif l!= None:
        #     return l
        if self.bpos.y>=1900:
            self.ink[4]=None
            self.song.pause()
            return 1
        
        self.detection()
        fill(248,245,214)
        
        rectMode(CORNER)
        rect(20,500,150,390,20)
        fill(128,209,200)
        pushMatrix()
        rotate(PI/2)
        text("score:"+str(self.score),700,-100)
        popMatrix()
    def drawAttractor(self):
        ellipseMode(CENTER)
        change=noise(0.1+frameCount/10)
        fill(148-20*change,0,211-change*100)
        ellipse(1610,720,410*(noise(0.1+frameCount/2,20+frameCount/2)/5+1),410*(noise(0.1+frameCount/2,0.3+frameCount/2)/5+1))
        
        pushMatrix()
        translate(1590,705)
        fill(0,0,0)
        ellipse(15*(noise(0.1+frameCount/2,20+frameCount/2)/2+1),15*(noise(0.1+frameCount/2,20+frameCount/2)/2+1),40,40)
        popMatrix()
        
    
    def drawColor(self):
        global c1,c2,c3,c1s,c2s,c3s
        
        
        if c1>=255:
            c1s=-random(3)
        elif c1<=0:
            cls=random(3)
        if c2>=255:
            c2s=-random(3)
        elif c2<=0:
            c2s=random(3)
        if c3>=255:
            c3s=-random(3)
        elif c3<=0:
            c3s=random(3)
            
        c1=constrain(c1+c1s,-1,256)
        c2=constrain(c2+c2s,-1,256)
        c3=constrain(c3+c3s,-1,256)
        colour=color(c1,c2,c3)
        fill(colour,50)
        beginShape()
        vertex(1250,800)
        vertex(1150,1400)
        vertex(1353,1200)
        vertex(1250,800)
        endShape()
        
        beginShape()
        vertex(200,1600)
        vertex(200,1800)    
        vertex(850,1800)
        

        endShape(CLOSE)
        
        beginShape()
        vertex(width-200,1600)
        vertex(width-200,1800)    
        vertex(width-850,1800)
        endShape(CLOSE)   
        
                  
        fill(248,245,214)
        beginShape()
        vertex(200,1400)
        vertex(200,1600)    
        vertex(850,1800)
        vertex(950,1800)    
        endShape(CLOSE)
        
        beginShape()
        vertex(width-200,1400)
        vertex(width-200,1600)    
        vertex(width-850,1800)
        vertex(width-950,1800)
            
        endShape(CLOSE)

        
        
        
        fill(128,209,200)
        
        beginShape()
        vertex(200,1400)    
        vertex(850,1750)
        vertex(850,1580)    
        endShape(CLOSE)
        
        beginShape()
        vertex(width-200,1400)    
        vertex(width-850,1750)
        vertex(width-850,1580)    
        endShape(CLOSE)
        
        beginShape()
        vertex(width-100,200)    
        vertex(width-70,1700)
        vertex(width-70,1800)
        vertex(width-200,1800)
        vertex(width-200,1400)      
        endShape(CLOSE)
        

        
        
    def detection(self):
        global u,i,o,p,s5,k,t1,t2,t3
        # print(dist(self.bpos.x,self.bpos.y,width-35,1720))
        
        if self.bpos.y<1400:
            if self.lv.x>90 or self.lv.x<-90 or self.lv.y>90 or self.lv.y<-90:
                for ii in range(int(random(2,3))):
                        self.particle.append(Ball(self.box2d,6,self.bpos.x-60+30*random(2),self.bpos.y-60+30*random(2),3,self.ball.c,int(random(180,420))))
                        self.particle[len(self.particle)-1].force1(Vec2(random(-500,500),random(-500,500)))
            
        
        
        if self.lv.y>0:
            if o*self.lv.y<0:
                # for ii in range(int(random(5,8))):
                #     # self.particle.append(Ball(self.box2d,6,self.bpos.x-60+30*random(2),self.bpos.y-60+30*random(2),3,self.ball.c,int(random(180,420))))
                #     # self.particle[len(self.particle)-1].force1(Vec2(random(-500,500),random(-500,500)))
                
                
                for x in range(10):
                    if self.bpos.x<350+(x+1)*45 and self.bpos.x>350+x*45 and self.bpos.y>760 and self.bpos.y<900:
                        s5[x].y+=50
                        self.ball.force1(Vec2(0,10000))
                        self.surface[4].clearBody()
                        self.surface[4]=Surface(self.box2d,s5,2)
                    
        o=self.lv.y
        k=self.lv.x    
        # if self.bpos.x<800 and self.bpos.x>350 and self.bpos.y<850 and self.bpos.y>600:
        for j in range(len(self.circles)):
            if self.circles[j]!=None:
                t=self.circles[j].box2d.getBodyPixelCoord(self.circles[j].body)
                if t.x>=width-100:
                    self.circles[j].force1(Vec2(0,1000))
                    if t.y<200:
                        self.circles[j].force1(Vec2(-1000,0))
                
                if dist(self.bpos.x,self.bpos.y,t.x,t.y)<=30+self.circles[j].r+7 and dist(self.bpos.x,self.bpos.y,t.x,t.y)>=30+self.circles[j].r-7 and self.circles[j].n <=2:
                    p+=2
                    if p==2: 
                        self.ball.body.setLinearVelocity(Vec2(-self.lv.x,-self.lv.y))
                        self.score+=5
                        self.circles[j].clearBody()
                        if self.circles[j].n !=2:
                            self.circles[j]=Circle(self.box2d,self.circles[j].r-8,self.circles[j].x,self.circles[j].y,self.colors[j][self.circles[j].n+1],1,self.circles[j].n+1)
                            
                            for ii in range(int(random(8,15))):
                                self.particle.append(Ball(self.box2d,6,self.bpos.x-60+30*random(2),self.bpos.y-60+30*random(2),3,self.ball.c,int(random(180,420))))
                                self.particle[len(self.particle)-1].force1(Vec2(random(-500,500),random(-500,500)))
                        else: 
                            self.circles[j]=Circle(self.box2d,self.circles[j].r-8,self.circles[j].x,self.circles[j].y,self.colors[j][self.circles[j].n+1],2,self.circles[j].n+1)
                            for ii in range(int(random(8,15))):
                                self.particle.append(Ball(self.box2d,6,self.bpos.x-60+30*random(2),self.bpos.y-60+30*random(2),3,self.ball.c,int(random(180,420))))
                                self.particle[len(self.particle)-1].force1(Vec2(random(-500,500),random(-500,500)))
                        p=0
                    
                if self.circles[j].t==2:
                    k+=1
                    if k==5:
                        if len(self.ink[j])==150:
                            self.ink[j].remove(self.ink[j][0])
                        self.ink[j].append(Ink(t,self.colors[j][self.circles[j].n],self.circles[j].r,1))
                        
                        k=0
                    
                if t.y>1900:
                    self.ink[j]=None
                    self.circles[j].clearBody()
                    self.circles[j]=None
                    
            
        if dist(self.bpos.x,self.bpos.y,width-35,1720)<=60:
            if self.o1s[0] !=None:
                self.ball.force1(Vec2(100,30000000))
                self.o1s[0].clearBody() 
                self.o1s[0]=None
                self.score+=50
                u=1
            
        if dist(self.bpos.x,self.bpos.y,width-35,1620)<=60:
            if self.o1s[1] !=None:
                self.ball.force1(Vec2(100,30000000))
                self.o1s[1].clearBody() 
                self.o1s[1]=None
                self.score+=50
                u=1
        if self.bpos.x>=width-100 and u==1 and i<=110:
            i+=1
            self.ball.force1(Vec2(0,300))
            if self.bpos.y<200:
                self.ball.force1(Vec2(-1000,0))
            if i==110:
                u=0
                i=0
                
        t2=constrain(t2+1,0,100)
        if dist(self.bpos.x,self.bpos.y,1610,720)<=205 :
            distance=dist(self.bpos.x,self.bpos.y,1610,720)
            if t1==0:
                t2=0
                v=Vec2((1610-self.bpos.x)*100*20/distance+1,-(720-self.bpos.y)*100*20/distance+1)
                self.ball.force1(v)
                
                

            elif t1==1:
                v=Vec2(-(1610-self.bpos.x)*50*20/distance+1,(720-self.bpos.y)*50*20/distance+1)
                self.ball.force1(v)
                for ii in range(int(random(2,3))):
                    self.particle.append(Ball(self.box2d,6,self.bpos.x-60+30*random(2),self.bpos.y-60+30*random(2),3,self.ball.c,int(random(180,420))))
                    self.particle[len(self.particle)-1].force1(Vec2(random(-500,500),random(-500,500)))
        if t2==30:
            t1=0
        if dist(self.bpos.x,self.bpos.y,1610,720)<=70:
            t1=1

        if self.bpos.y<=250 and self.bpos.y>200:
            
            for ii in range(int(random(2,3))):
                self.particle.append(Ball(self.box2d,6,self.bpos.x-60+30*random(2),self.bpos.y-60+30*random(2),3,self.ball.c,int(random(180,420))))
                self.particle[len(self.particle)-1].force1(Vec2(random(-500,500),random(-500,500)))
                
        if self.bpos.y<1400 and self.bpos.y>200 and self.bpos.x<1200 and self.bpos.x>800:
            self.ball.force1(Vec2(0,480))
        
        if self.bpos.y<=200:
            
            noFill()
            stroke(0)
            beginShape()
            for b in range(5):
                vertex(self.bpos.x-50+100*noise(b+frameCount/20),20)
                for i in range(int(random(1,5))):
                    vertex(self.bpos.x-100+i*100*noise(b+i+frameCount/20),(self.bpos.y-10)/5*i)
                vertex(self.bpos.x,self.bpos.y)
                endShape()
            
            self.ball.force1(Vec2(100,600))
            
        if dist(self.bpos.x,self.bpos.y,300,300)<=70:
            self.ball.c=color(73,45,34)
        if dist(self.bpos.x,self.bpos.y,300,700)<=70:
            self.ball.c=color(1,132,127)
        if dist(self.bpos.x,self.bpos.y,600,500)<=150:
            self.ball.c=color(249,210,228) 
                
         
            
    def drawBoundary(self):
        for i in self.ink:
            if i!=None:
                for j in i:
                    if j!=None:
                        j.display()
        for i in self.boundary:
            i.display()
        for i in range(len(self.surface)):
            if i !=5:
                self.surface[i].display()
        for i in self.o1s:
            if i !=None: 
                i.display()
        for i in self.circles:
            if i !=None:
                i.display()
        for i in self.particle:
            if i!=None:
                i.display()
                i.life-=1
                if i.life==0:
                    i.clearBody()
                    self.particle.remove(i)
        
    def drawBall(self):
        global t3
        self.score+=0.01
        self.bpos=self.ball.display()
        a = self.ball.body.getAngle()
        pushMatrix()
        translate(self.bpos.x,self.bpos.y)
        rotate(-a)  
        fill(self.ball.c)
        noStroke
        ellipseMode(CENTER)
        ellipse(0,0,self.ball.r*2,self.ball.r*2)
        popMatrix()
        if self.score>=0:
            pushMatrix()
            translate(self.bpos.x,self.bpos.y)
            for tt in range(int(self.score)/5):
                rotate(frameCount/3+TWO_PI/(int(self.score)/5)*tt)
                ellipseMode(CENTER)
                fill(c1,c2,c3)
                ellipse(self.ball.r,self.ball.r,10,10)
                
            popMatrix()
        t3+=1
        if t3>=4:
            if self.bpos.y>=200:
                if len(self.ink[4])==200:
                    self.ink[4].remove(self.ink[4][0])
                self.ink[4].append(Ink(self.bpos,self.ball.c,self.ball.r,1))
                t3=0
    def drawBridge(self):
        
        pushMatrix()
        translate(300,300)
        rotate(frameCount/10)
        fill(73,45,34)
        rectMode(CENTER)
        rect(0,0,100,100)
        popMatrix()
        
        pushMatrix()
        translate(300,700)
        rotate(frameCount/10)
        fill(1,132,127)
        ellipse(0,0,100*(noise(0.1+frameCount/2,20+frameCount/2)/2+1),100*(noise(0.1+frameCount/2,0.3+frameCount/2)/2+1))
        popMatrix()
        
        pushMatrix()
        translate(600,500)
        rotate(frameCount/10)
        fill(249,210,228) 
        ellipse(0,0,200*(noise(0.1+frameCount/2,20+frameCount/2)/2+1),150*(noise(0.1+frameCount/2,0.3+frameCount/2)/2+1))
        popMatrix()
        
        # rectMode(CENTER)
        # rect(width/2,400,300,20)
        
       
        
        
class RectBoundary:
    def __init__(self,b,xx,yy,ww,hh,tt):
        self.box2d=b
        self.x=xx
        self.y=yy
        self.w=ww
        self.h=hh
        self.t=tt
        
        bd =BodyDef()
        if self.t==1:
            bd.type = BodyType.STATIC
        elif self.t==2 or self.t==3:
            bd.type = BodyType.DYNAMIC
            
        center = self.box2d.coordPixelsToWorld(self.x,self.y)
        bd.position.set(center)
        if self.t==1:
            bd.fixedRotation = 1
        elif self.t==2:
            bd.fixedRotation = 0
        bd.linearDamping = 0.8
        bd.angularDamping = 0.9
        bd.bullet = 1
        
        self.body=self.box2d.createBody(bd)
        self.ps =PolygonShape()
        
        box2dw = self.box2d.scalarPixelsToWorld(self.w/2)    
        box2dh = self.box2d.scalarPixelsToWorld(self.h/2) 
        if self.t==1 or self.t==3:   
            self.ps.setAsBox(box2dw,box2dh)   
        if self.t==2:
            self.vs=[self.box2d.vectorPixelsToWorld(Vec2(0,-1)),
                self.box2d.vectorPixelsToWorld(Vec2(0,1)),
                self.box2d.vectorPixelsToWorld(Vec2(self.w,self.h/2)),
                self.box2d.vectorPixelsToWorld(Vec2(self.w+10,5)),
                self.box2d.vectorPixelsToWorld(Vec2(self.w+10,-5)),
                self.box2d.vectorPixelsToWorld(Vec2(self.w,-self.h/2))
                ]
            self.ps.set(self.vs,len(self.vs))
            # self.ps.setAsBox(box2dw,box2dh)
        fd = FixtureDef()
        fd.shape = self.ps   
        fd.friction = 0   
        fd.restitution = 1 
        fd.density = 1 
        self.body.createFixture(fd)
        
        
    def display(self):
        if self.t==1:
            fill(128,209,200)
            noStroke()
            rectMode(CENTER)
            rect(self.x,self.y,self.w,self.h)
        if self.t==2:
            pos = self.box2d.getBodyPixelCoord(self.body);
            a = self.body.getAngle();
            rectMode(CENTER)
            pushMatrix()
            translate(pos.x,pos.y)
            rotate(-a)
            fill(175)
            stroke(0)
            beginShape()
            for i in range(len(self.vs)):
                v=self.box2d.vectorWorldToPixels(self.ps.getVertex(i))
                vertex(v.x,v.y)
            endShape(CLOSE)
            popMatrix()
        if self.t==3:
            pos = self.box2d.getBodyPixelCoord(self.body);
            a = self.body.getAngle();
            pushMatrix()
            translate(pos.x,pos.y)
            rotate(-a)
            fill(128,209,200)
            noStroke()
            rectMode(CENTER)
            rect(0,0,self.w,self.h)            
            popMatrix()

        
    def clearBody(self):
        self.box2d.destroyBody(self.body)    
        
class Ball:
    def __init__(self,b,rr,xx,yy,tt,cc,l):
        self.box2d=b
        self.x=xx
        self.y=yy
        self.r=rr
        self.t=tt
        self.c=cc
        self.life=l
        bd =BodyDef()
        bd.type = BodyType.DYNAMIC
        center = self.box2d.coordPixelsToWorld(self.x,self.y)
        bd.position.set(center)
        bd.fixedRotation = 1
        bd.linearDamping = 0.1
        bd.angularDamping = 0.2
        bd.bullet = 1
        
        self.body=self.box2d.createBody(bd)
        cs = CircleShape()
        cs.m_radius = self.box2d.scalarPixelsToWorld(self.r)
        
        fd = FixtureDef();
        fd.shape = cs   
        fd.friction = 0   
        fd.restitution = 0.8
        fd.density = 0.5 
        self.body.createFixture(fd)
        
    def display(self):
        if self.t==1:
            pos = self.box2d.getBodyPixelCoord(self.body)
            
            return pos
        
        if self.t==2:
            pos = self.box2d.getBodyPixelCoord(self.body)
            return pos
        
        if self.t==3:
            pos = self.box2d.getBodyPixelCoord(self.body);
            a = self.body.getAngle();
            pushMatrix()
            translate(pos.x,pos.y)
            rotate(-a)
            fill(self.c)
            noStroke()
            ellipseMode(CENTER)
            ellipse(0,0,self.r,self.r)            
            popMatrix()
        
    def force1(self,v):
        self.body.applyForce(v, self.body.getWorldCenter())
    
    def clearBody(self):
        self.box2d.destroyBody(self.body)    

class Circle:
    def __init__(self,b,rr,xx,yy,cc,tt,nn):
        self.box2d=b
        self.x=xx
        self.y=yy
        self.r=rr
        self.c=cc
        self.t=tt
        self.n=nn
        
        bd =BodyDef()
        if self.t==1:
            bd.type = BodyType.STATIC
        elif self.t==2:
            bd.type = BodyType.DYNAMIC
        center = self.box2d.coordPixelsToWorld(self.x,self.y)
        bd.position.set(center)
        bd.fixedRotation = 1
        bd.linearDamping = 0.1
        bd.angularDamping = 0.2
        bd.bullet = 1
        
        self.body=self.box2d.createBody(bd)
        cs = CircleShape()
        cs.m_radius = self.box2d.scalarPixelsToWorld(self.r)
        
        fd = FixtureDef();
        fd.shape = cs   
        fd.friction = 0   
        fd.restitution = 1 
        fd.density = 0.5 
        self.body.createFixture(fd)
        
    def display(self):
        pos = self.box2d.getBodyPixelCoord(self.body)
        a = self.body.getAngle()
        pushMatrix()
        translate(pos.x,pos.y)
        rotate(-a)  
        fill(self.c)
        noStroke()
        ellipseMode(CENTER)
        ellipse(0,0,self.r*2,self.r*2)
        popMatrix()
        return pos
    
    def clearBody(self):
        self.box2d.destroyBody(self.body)   
    def force1(self,v):
        self.body.applyForce(v, self.body.getWorldCenter())
        
class Surface:
    
    def __init__(self,b,vertexs,tt):
        self.box2d=b
        self.vs1=vertexs
        self.vs2=[]
        self.chain = ChainShape()
        self.t=tt
        for i in range(len(self.vs1)):
            self.vs2.append(self.box2d.coordPixelsToWorld(self.vs1[i]))
        self.chain.createChain(self.vs2,len(self.vs2))
        bd =BodyDef()
        bd.type = BodyType.STATIC
        self.body=self.box2d.createBody(bd)
        if self.t==1:
            fd = FixtureDef();
            fd.shape = self.chain   
            fd.friction = 0.5   
            fd.restitution = 0.1
            fd.density = 0 
            self.body.createFixture(fd)
        elif self.t==2:
            fd = FixtureDef();
            fd.shape = self.chain   
            fd.friction = 0.5   
            fd.restitution = 0.2
            fd.density = 0 
            self.body.createFixture(fd)
        
    def display(self):
        noFill()
        stroke(0)
        strokeWeight(1)
        beginShape()
        for i in self.vs1:
            vertex(i.x,i.y)
        endShape()

    def clearBody(self):
        self.box2d.destroyBody(self.body)        
class Bounder:
    def __init__(self,b,att,tt):
        self.box2d=b
        self.at=att
        self.t=tt
        # s1=[Vec2(width/2-100,1581),Vec2(width/2-30,height-200)]
        # self.ss1=Surface(self.box2d,s1,2)
        if self.t==1:
            self.ss2=RectBoundary(self.box2d,width/2-146,1584,2,2,1)
            self.ss1=RectBoundary(self.box2d,width/2-146,1584,125,25,2)
        elif self.t==2:
            self.ss2=RectBoundary(self.box2d,width/2+146,1584,2,2,1)
            self.ss1=RectBoundary(self.box2d,width/2+146,1584,125,25,2)
            
        self.rjd=RevoluteJointDef()
        
        self.rjd.initialize(self.ss1.body,self.ss2.body,self.ss2.body.getWorldCenter())
        # self.box2d.coordPixelsToWorld(Vec2(width/2-100,1581))
        self.rjd.enableLimit = True;
        if self.t==1:
            self.rjd.lowerAngle = -PI/2;
            self.rjd.upperAngle = PI/4;
        elif self.t==2:
            self.rjd.lowerAngle = -PI/4+PI;
            self.rjd.upperAngle = PI*1.5;
        self.rjd.enableMotor = 1
        
        self.rjd.motorSpeed = PI*2
        self.rjd.maxMotorTorque = 1000000.0
        self.joint=self.box2d.world.createJoint(self.rjd)
    
    def display(self,kl):
        if self.t==1:
            # if keyPressed:
            #     if key=="A" or key=="a":
            #          self.joint.setMotorSpeed(-PI*4)
            # else: 
            #     self.joint.setMotorSpeed(PI*2)
            
            if kl[0]==1:
                self.joint.setMotorSpeed(-PI*4)
            else: 
                self.joint.setMotorSpeed(PI*2)
        if self.t==2:
            if kl[1]==1:
                self.joint.setMotorSpeed(PI*4)
            else: 
                self.joint.setMotorSpeed(-PI*2)
        
        self.ss1.display()
        self.ss2.display()
    
    def toggleMotor(self):
        motorstaus = self.joint.isMotorEnabled()
        if motorstaus==True:
            self.joint.enableMotor(1)



class Bounder2:
    def __init__(self,b):
        self.box2d=b
        self.ss2=RectBoundary(self.box2d,width/2,400,2,2,1)
        self.ss1=RectBoundary(self.box2d,width/2,400,300,20,3)
        self.rjd=RevoluteJointDef()
        self.rjd.initialize(self.ss1.body,self.ss2.body,self.ss2.body.getWorldCenter())
        self.rjd.enableMotor = 1
        self.rjd.motorSpeed = PI*2
        self.rjd.maxMotorTorque = 1000000.0
        self.joint=self.box2d.world.createJoint(self.rjd)

    def display(self):
        self.ss1.display()
        self.ss2.display()

    def toggleMotor(self):
        motorstaus = self.joint.isMotorEnabled()
        if motorstaus==True:
            self.joint.enableMotor(1)








class Object1:
    
    def __init__(self,b,xx,yy,ll,tt):
        self.box2d=b
        self.t=tt
        self.list=ll
        self.x=xx
        self.y=yy
        bd =BodyDef()
        center = self.box2d.coordPixelsToWorld(self.x,self.y)
        bd.position.set(center)
        bd.type = BodyType.STATIC
        bd.linearDamping = 0.8
        bd.angularDamping = 0.9
        bd.bullet = 1
        self.body=self.box2d.createBody(bd)
        self.ps =PolygonShape()
        for i in range(len(ll)):
            self.list[i]=self.box2d.vectorPixelsToWorld(ll[i])        
        self.ps.set(self.list,len(self.list))
        fd = FixtureDef()
        fd.shape = self.ps   
        fd.friction = 0   
        fd.restitution = 1 
        fd.density =0 
        self.body.createFixture(fd)

    def display(self):
        pos = self.box2d.getBodyPixelCoord(self.body);
        a = self.body.getAngle()
        pushMatrix()
        rectMode(CENTER)
        
        translate(pos.x,pos.y)

        rotate(-a)
        fill(175)
        stroke(0)
        beginShape()
        for i in range(len(self.list)):
            v=self.box2d.vectorWorldToPixels(self.ps.getVertex(i))
            vertex(v.x,v.y)
        endShape(CLOSE)
        popMatrix()
        
    def clearBody(self):
        self.box2d.destroyBody(self.body)
        


class Ink:
    def __init__(self,pos,cc,rr,tt):
        self.p=pos
        self.c=cc
        self.t=tt
        self.r=rr
    
    def display(self):
        if self.t==1:
            noStroke()
            fill(self.c,10)
            ellipse(self.p.x,self.p.y,self.r*2,self.r*2)
        
        
        
        
