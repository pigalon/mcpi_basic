import time
from mcpi.minecraft import Minecraft
import mcpi.block as block


mc = Minecraft.create()

x,y,z = mc.player.getTilePos()
mc.setBlocks(x+1, y, z+1, x+11, y+11, z+11, block.WOOL.id, 4)
