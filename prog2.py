import time
from mcpi.minecraft import Minecraft

mc = Minecraft.create()

mc.postToChat("coucou les amis")
while True:
    time.sleep(1)
    x,y,z = mc.player.getTilePos()

    mc.postToChat("x:"+str(x)+" y:"+str(y)+" z:"+str(z))