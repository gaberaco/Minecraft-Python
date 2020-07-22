#Magic Wand
from mcpi.minecraft import Minecraft
import time

mc = Minecraft.create()

while True: 
    hits = mc.events.pollBlockHits()

    for i in hits: 
        x = i.pos.x
        y = i.pos.y
        z = i.pos.z

        blockType = mc.getBlock(x,y,z)
        if blockType == 12:
            mc.postToChat("You Hit Sand")
            mc.setBlock(x,y,z,57)
