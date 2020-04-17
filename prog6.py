import time
from mcpi.minecraft import Minecraft
import keyboard

def construire_blocs_tnt(x, y, z):
    mc.setBlocks(x+1, y, z+1, x+11, y+11, z+11, 46, 2)

mc = Minecraft.create()
while True:
    x,y,z = mc.player.getTilePos()
    try:
        if keyboard.is_pressed('ctrl+p'):
            construire_blocs_tnt(x, y, z)
        elif keyboard.is_pressed('ctrl+esc'):
            break
        else:
            pass
    except:
        break



