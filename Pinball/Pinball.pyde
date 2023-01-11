add_library('sound')
add_library('minim')


from startInterface import StartInterface
from settingInterface import SettingInterface
from gameInterface import GameInterface
from interface import Interface #Parent class
from endInterface import EndInterface

add_library('jbox2d')
add_library('box2d_processing')


from shiffman.box2d import *
from org.jbox2d.dynamics import *
from org.jbox2d.common import *
from org.jbox2d.collision.shapes import *
from org.jbox2d.dynamics.joints import *
from org.jbox2d.dynamics.contacts import *

def setup():
    global startI,logoCond,isExit,condition,settingI,gameI,box2d,mySounds,volume,interface,myFonts
    global isExit,endI,player,timep,isStart,keyList,restart,pp
    keyList=[0,0]
    pp=0
    restart=0
    isStart=0
    timep=0
    isExit =0
    logoCond=1
    volume=1
    condition =1
    size(2000,1800)
    minim =Minim(this)
    player =minim.loadFile("music1.mp3")
    player2=minim.loadFile("TheFirstLayer.mp3")
    player3=minim.loadFile("EldenRing.mp3")
    mySounds =[SoundFile(this,"UI1.wav"),(this,"Collision1.wav")]
    myFonts =[createFont("Comic Sans MS", 100),createFont("Lucida Handwriting Italic",100),createFont("Comic Sans MS", 140)
              ,createFont("Harrington",200),createFont("Lucida Handwriting Italic",30)]
    startI = StartInterface(myFonts,mySounds,volume,loadImage("eyeMouse.png"),player3)
    settingI =SettingInterface(myFonts,mySounds,volume,loadImage("icon1.png"))
    gameI = GameInterface(myFonts,mySounds,volume,player2)#box2D
    endI =  EndInterface(myFonts,mySounds,volume,loadImage("icon1.png"),player)
    
def draw():
    global condition,volume,startI,settingI,timep,isStart,restart,pp
    # if(logoCond):
    #     global logoCond
    #     logoCond=0
    #     startLogo()
    # Because of the bug of videoLibrary 
    # in Processing 3.5.4 in windows,this code block is deserted
    
    #startInterface
    if(condition ==1):
        if millis()-timep>600:
            if startI.working()!=None:
                condition=startI.working()
                if pp==0:
                    background(255,255,255,20)
                    pp=1
                
                
                
    
    #gameInterface-unfinished
    
    elif(condition ==2):
    #   gaming()
        
        if restart==1:
            restart=0
            isStart=0
        
        if isStart==0:
            gameI.preWorking()
            isStart=1
            
        t=gameI.working(keyList)
        if t==1:
            condition=4
        elif t==2:
            condition=3
            
    #settingInterface
    elif condition ==3:
        q=settingI.working()
        if type(q)==float:
            # print(q)
            changeVolume(q)
        if q==3:
            condition=1
            
    #endInterface
    elif(condition== 4):
        # print(endI.working())
        p=endI.working()
        if p!=None:
            timep=millis()
            # print(timep)
            condition = p
            restart=1
        # print("gameOver")
        
    if(isExit==1):
        exit()    
        

def changeVolume(vo):
    global player
    settingI.volume=vo
    startI.volume=vo
    settingI.button1.volume=vo
    settingI.button2.volume=vo
    settingI.button3.volume=vo
    startI.button1.volume=vo
    startI.button2.volume=vo
    startI.button3.volume=vo
    endI.volume=vo
    gameI.volume=vo
    
def keyPressed():
    global keyList
    if keyList[0]==0:
        if key=="a" or key=="A":
            keyList[0]=1
    if keyList[1]==0:
        if key=="d" or key=="D":
            keyList[1]=1
            
def keyReleased():
    if keyList[0]==1:
        if key=="a" or key=="A":
            keyList[0]=0
    if keyList[1]==1:
        if key=="d" or key=="D":
            keyList[1]=0
            
def beginContact():
    pass
