#Block SHOOTER
from mcpi.minecraft import Minecraft
import time
mc = Minecraft.create()

while True:
    x,y,z = mc.player.getPos()
    for i in range(1,20):
        mc.setBlock(x,y,z+i,49)  #this is the block that shoots
        time.sleep(.1)
        mc.setBlock(x,y,z+i,0)
        
