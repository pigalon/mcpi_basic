from mcpi.minecraft import Minecraft
#import keyboard
import mcpi.block as block

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
        print('coordonnees de la position x :' + str(self.x) +
            '; y : ' + str(self.y) + '; z : ' + str(self.z))

##################################################################

class Maison:
    longueur = 0
    hauteur = 0
    profondeur = 0
    position_debut = None

    def __init__(self, longeur, hauteur, profondeur):
        self.longueur = longeur
        self.hauteur = hauteur
        self.profondeur = profondeur

    def init_position_debut(self, x, y, z):
        self.position_debut = Position(x+3, y, z+3)

    def construire_murs(self):
        fin = Position(self.position_debut.x+self.longueur, 
                        self.position_debut.y+self.hauteur, self.position_debut.z+self.profondeur)
        mc.setBlocks(self.position_debut.x, self.position_debut.y, 
                        self.position_debut.z, fin.x, fin.y, fin.z, block.STONE.id)

    def construire_vide(self):
        debut = Position(self.position_debut.x+1, self.position_debut.y+1,
                        self.position_debut.z+1)
        fin = Position(debut.x+self.longueur-2, debut.y+self.hauteur-2,
                        debut.z+self.profondeur-2)
        mc.setBlocks(debut.x, debut.y, debut.z, fin.x,
                        fin.y, fin.z, block.AIR.id)

    def construire_maison(self, x, y, z):
        self.init_position_debut(x, y, z)
        self.construire_murs()
        self.construire_vide()
        # construire_toit
        # construire_fenetres
        # construire_porte
        # construire etage
        # construire escalier
        # mettre moquette
        print('construire maison')

# Main

LG_MAISON = 12
HT_MAISON = 8
PR_MAISON = 8
TYPE_BLOCK = 1

mc = Minecraft.create()

x, y, z = mc.player.getTilePos()

maison = Maison(LG_MAISON, HT_MAISON, PR_MAISON)
maison.construire_maison(x+3, y, z+3)
