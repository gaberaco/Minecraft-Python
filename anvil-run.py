#Anvil Run
from mcpi.minecraft import Minecraft
import random
import time
mc = Minecraft.create()
mc.postToChat("RUN FOR COVER!!!!!")
anvils = 500
while (anvils > 0):
    x,y,z = mc.player.getPos()
    rX = random.randint(-20,20)
    rZ = random.randint(-20,20)
    mc.setBlock(x+rX,y+40,z+rZ,145) 
    anvils = anvils - 1
    mc.postToChat(anvils)
    time.sleep(.1)
mc.postToChat("You Win!")
