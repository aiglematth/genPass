#Auteur --> aiglematth
"""
Fichier des outils de la gui
"""
#Imports
import tkinter
import tkinter.scrolledtext as tkScroll
import constantes
import genPass
import config

#Classes
class Main(tkinter.Tk):
    """
    Classe dérivée de tkinter.Tk, crée la fenêtre principale
    """
    def __init__(self):
        """
        Constructeur de la classe Main
        """
        tkinter.Tk.__init__(self)
        #Variables de la fenêtre
        self.nombreDeChars = tkinter.IntVar()

        #Caractéristiques de la fenêtre
        self.geometry(constantes.geometry)
        self.title(constantes.title)
        self.resizable(False, False)

        #Appel des widgets
        self.widgets()

    def widgets(self):
        """
        Méthode qui appel tout les widgets nécessaires à la GUI
        :return: None
        """
        labelTitre = tkinter.Label(self, text=constantes.title)
        labelTitre.place(x=constantes.intSize[0]//2.25, y=constantes.intSize[1]//20)

        labelNbr = tkinter.Label(self, text="Nombre de charactères : ")
        labelNbr.place(x=constantes.intSize[0]//50, y=constantes.intSize[1]//4)

        nbrChar = tkinter.Entry(self, textvariable=self.nombreDeChars)
        nbrChar.place(x=constantes.intSize[0]//2,  y=constantes.intSize[1]//4)

        bouttonGen = tkinter.Button(self, text="Générer", command=self.bouttonGen)
        bouttonGen.place(x=constantes.intSize[0]//2.25, y=constantes.intSize[1]//3)

    def bouttonGen(self):
        """
        Fonction qui génère le mot de passe
        :return: None
        """
        password = genPass.GenPass()
        if self.nombreDeChars.get() <= 0 or self.nombreDeChars.get() == None:
            self.nombreDeChars.set(config.defaultSize)
        password.defineMdp(size=self.nombreDeChars.get(), chars=config.typeOfChars)

        scrText = tkScroll.ScrolledText(self, wrap="char", width=constantes.intSize[0]//9)
        scrText.place(x=constantes.intSize[1]//50, y=constantes.intSize[1]//2.5)
        scrText.insert(index=tkinter.INSERT, chars="##### BEGIN #####\n")
        scrText.insert(index=tkinter.INSERT, chars=password.getMdp())
        scrText.insert(index=tkinter.INSERT, chars="\n##### END #####")
