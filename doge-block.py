#DodgeBlockXDXDXDDXd
from mcpi.minecraft import Minecraft
import time
import random
mc = Minecraft.create()
d = 5    # set difficulty
score = 0
mc.postToChat("3")
time.sleep(1)
mc.postToChat("2")
time.sleep(1)
mc.postToChat("1")
time.sleep(1)
mc.postToChat("GO!!!")
#move player and spawn arena
x,y,z = mc.player.getPos()
mc.setBlocks(x+d,y+20,z+d,x-d,y+20,z-d,1)
mc.player.setPos(x,y+22,z)
time.sleep(1)
#make dat laavvavavva
x,y,z = mc.player.getPos()
lavaZ = z - d
count = 50
while (count>0):
    pX,pY,pZ = mc.player.getPos()
    if pY < y:
        mc.postToChat("You lose! Score: %s" %score)
        break
    rX = random.randint(-d,d)
    for i in range(11):    
        mc.setBlock(x+rX,y,lavaZ+i,11)
        time.sleep(.1)
        mc.setBlock(x+rX,y,lavaZ+i,0)
    score = score + 1
    count = count - 1
    mc.postToChat(count)
if (count == 0):
    mc.postToChat("You win!!! Score: %s" %score)
