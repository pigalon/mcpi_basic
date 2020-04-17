from mcpi.minecraft import Minecraft
import keyboard
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
    
    
    def construire_maison(x, y, z):
        # construire_mur
        # construire_vide
        # construire_toit
        # construire_fenetres
        # construire_porte
        # construire etage
        # construire escalier
        # mettre moquette
        print('construire maison')


    def construire_murs(x, y, z, longueur, hauteur, profondeur, type):
        debut = Position(x+3, y, z+3)
        debut.afficher_position()
        fin = Position(debut.x+longueur, debut.y+hauteur, debut.z+profondeur)
        mc.setBlocks(debut.x, debut.y, debut.z, fin.x, fin.y, fin.z, type)


    def construire_vide(x, y, z, longueur, hauteur, profondeur):
        debut = Position(x+3, y, z+3)
        debut.afficher_position()
        fin = Position(debut.x+longueur, debut.y+hauteur, debut.z+profondeur)
        mc.setBlocks(debut.x, debut.y, debut.z, fin.x,
                    fin.y, fin.z, block.EMPTY.id)


# mettre dans une classe maison et associer les coordonnées à l amaison
# nous ne sommes plus sur les coordonnées du joureur

# def construire_vide(x, y, z, longueur, hauteur, profondeur, type):
#     debut = Position(x+3, y, z+3)
#     debut.afficher_position()
#     fin = Position(debut.x+longueur, debut.y+hauteur, debut.z+profondeur)
#     mc.setBlocks(debut.x, debut.y, debut.z, fin.x, fin.y, fin.z, type)


# def construire_blocs_tnt(x, y, z):
#     mc.setBlocks(x+1, y, z+1, x+11, y+11, z+11, 46, 2)
LG_MAISON = 12
HT_MAISON = 8
PR_MAISON = 8
TYPE_BLOCK = 1

mc = Minecraft.create()

x, y, z = mc.player.getTilePos()

construire_murs(x=x, y=y, z=z, longueur=LG_MAISON, hauteur=HT_MAISON, profondeur=PR_MAISON, TYPE_BLOCK)
