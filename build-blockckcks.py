#BobDaBuilder
from mcpi.minecraft import Minecraft

mc = Minecraft.create()

x,y,z = mc.player.getPos()

#Cube size variables
L = 10
H = 40
W = 10

#create a cube made of stone
mc.setBlocks(x,y,z,x+L,y+H,z+W,155)

#make it hollow
L = 9
H = 39
W = 9
mc.setBlocks(x+1,y+1,z+1,x+L,y+H,z+W,0)
