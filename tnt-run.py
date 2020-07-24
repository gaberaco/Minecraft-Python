#TNT Run
from mcpi.minecraft import Minecraft
import random
import time
mc = Minecraft.create()
mc.postToChat("RUN!!!!!!!")
tnt = 500
while (tnt > 0):
    x,y,z = mc.player.getPos()
    rX = random.randint(-20,20)
    rZ = random.randint(-20,20)
    mc.setBlock(x+rX,y+41,z+rZ,152) 
    mc.setBlock(x+rX,y+40,z+rZ,46)
    mc.setBlock(x+rX,y+41,z+rZ,0) 
    tnt = tnt - 1
    mc.postToChat(tnt)
    time.sleep(.5)
mc.postToChat("You Win!")
