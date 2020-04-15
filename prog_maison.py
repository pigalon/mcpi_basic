from mcpi.minecraft import Minecraft
import keyboard

###########################################################
class Position:
    x = 0
    y = 0
    z = 0

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def afficher_position(self):
        print('coordonnees de la position x :' + str(self.x) + '; y : ' + str(self.y) + '; z : ' + str(self.z) )

##################################################################




# def construire_blocs_tnt(x, y, z):
#     mc.setBlocks(x+1, y, z+1, x+11, y+11, z+11, 46, 2)

LG_MAISON = 12
HT_MAISON = 8
PR_MAISON = 8

mc = Minecraft.create()


x,y,z = mc.player.getTilePos()


debut = Position(x+3,y,z+3)
debut.afficher_position()

fin = Position(debut.x+LG_MAISON, debut.y+HT_MAISON, debut.z+PR_MAISON)

mc.setBlocks(debut.x, debut.y, debut.z, fin.x, fin.y, fin.z, 1)


