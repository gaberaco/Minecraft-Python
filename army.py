#Army
from mcpi.minecraft import Minecraft
import time
mc = Minecraft.create()


while True:
    #Iron Golems U can do snow golems as well
    x,y,z = mc.player.getPos()
    mc.setBlock(x,y,z,42)
    mc.setBlock(x,y+1,z,42)
    mc.setBlock(x,y+1,z+1,42)
    mc.setBlock(x,y+1,z-1,42)
    mc.setBlock(x,y+2,z,86)
    time.sleep(.1)
