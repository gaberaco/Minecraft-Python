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
            blocks = mc.getBlocks(x+20,y+20,z+20,x-20,y-20,z-20)
            count = 0
            for b in blocks:
                #mc.postToChat(b)
                if b == 56:
                    count = count +1
            mc.postToChat( str(count)  +"Diamond Blocks found")
