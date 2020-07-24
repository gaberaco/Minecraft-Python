#Auto Tunneler
from mcpi.minecraft import Minecraft
import time
mc = Minecraft.create()

mc.postToChat("Auto Tunneler Start :)")

count = 10
sz = 20   # size of tunnel
while (count > 0):
    x,y,z = mc.player.getPos()
    mc.setBlocks(x-sz,y-sz,z-sz,x+sz,y+sz,z+sz,0)
    count = count - 1
    mc.postToChat(count)
    time.sleep(1)
mc.postToChat("Auto Tunneler Complete")
