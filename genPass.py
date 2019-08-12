#Auteur --> aiglematth
"""
Ceci est le fichier qui contient les outils de génération des passwords
"""
#Imports
import config
from random import randint

#Classe
class GenPass():
    """
    Classe qui génerera un mot de passe aléatoire
    """
    def __init__(self):
        """
        Constructeur de la classe GenPass
        """
        self.mdp = ""

    def getMdp(self):
        """
        getteur de self.mdp
        :return: self.mdp
        """
        return self.mdp

    def setNullMdp(self):
        """
        reinitialise self.mdp à ""
        :return: None
        """
        self.mdp = ""

    def defineMdp(self, size, chars=config.typeOfChars):
        """
        définit un mot de passe selon une taille et des charactères données
        :param size:   taille du mot de passe
        :param chars:  liste des chars qui constitueront le mot de passe
        :return:       None
        """
        self.setNullMdp()
        for i in range(0, size):
            index = randint(0, len(chars)-1)
            self.mdp += chars[index]
