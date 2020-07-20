#Ore
from mcpi.minecraft import Minecraft

mc = Minecraft.create()

def oreFinder(id,blockName,ind,*args):
    x,y,z = mc.player.getPos()
    for i in range (1,64):
        blockFound = mc.getBlock(x,y-i,z)
        if blockFound == id:
            mc.postToChat(blockName + "found : " +str(i)+ "blocks below.")
            mc.setBlock(x,y,z,ind,*args)
            break

while True: 
    oreFinder(129,"Emerald",171,5)
    oreFinder(56,"Diamond",171,3)
    oreFinder(21,"Lapis",171,11)
    oreFinder(15,"Iron",171,12)
    oreFinder(73,"Redstone",171,14)
    oreFinder(16,"Coal",171,15)
    oreFinder(14,"Gold",171,4)
