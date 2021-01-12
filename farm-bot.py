#Farm Bot
from mcpi.minecraft import Minecraft
mc = Minecraft.create()
mc.postToChat("Farm Bot Enabled")


seeds = 100
while(seeds > 0):
    x,y,z = mc.player.getPos()
    groundBlock = mc.getBlock(x,y-1,z)
    #check if ground is grass block
    if groundBlock == 2:
        mc.setBlock(x,y-1,z,60)
        mc.setBlock(x,y,z,141)
        seeds = seeds - 1
        seedsChat = str(seeds)
        mc.postToChat("Seed Planted. "+seedsChat+"Seeds Remaining")
mc.postToChat("Farm Bot Disabled")


