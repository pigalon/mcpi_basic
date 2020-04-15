import time
from mcpi.minecraft import Minecraft

mc = Minecraft.create()

x,y,z = mc.player.getTilePos()
mc.player.setTilePos(0,0,0)