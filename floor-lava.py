# the floor be lavaa
from mcpi.minecraft import Minecraft
import time 
import random

mc = Minecraft.create()
x,y,z = mc.player.getPos()
highScore = 0
def GameStart(): 
    #Startup
    mc.setBlocks(x,y+5,z,x+3,y+5,z+3,20)
    mc.player.setPos(x,y+10,z)

    mc.postToChat("Get Ready!")
    time.sleep (2.5)

    points = 0

    x2,y2,z2 = mc.player.getPos()
    while True:
        x,y,z = mc.player.getPos()



        standBlock = mc.getBlock(x,y-1,z)
        points = points+5
        if y  <y2:
            mc.postToChat("YOU LOSE :(")
            mc.postToChat("Your Score was %s points" % points)
            if points > highScore:
                mc.postToChat("New High Score: %s points" %highScore) 
                highScore = points
            else:
                mc.postToChat("High Score: %s points" %highScore)
            time.sleep(3)
            break
        else:
            mc.postToChat("Jump!")
        #the bigger the number,the harder it is
            rZ = random.randint(1,3)
            rX = random.randint(-2,1)
            mc.setBlock(x+rX,y-1,z+rZ,20)
            #less time is more hard 
            time.sleep(1.5)
            mc.setBlock(x,y-1,z,0)
            time.sleep(1)
GameStart()
