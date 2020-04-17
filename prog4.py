import time
from mcpi.minecraft import Minecraft
import mcpi.block as block


mc = Minecraft.create()

x,y,z = mc.player.getTilePos()
mc.setBlock(x, y, z, block.WOOL.id, 4)