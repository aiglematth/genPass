#Auteur --> aiglematth
"""
Fichier de configuration des options du générateur
"""

#Imports
import constantes

"""
typeOfChars définit quels charactères pourront se trouver dans le mot de passe, peut prendre :
    - constantes.minuscules qui correspond à "abcdefghijklmnopqrstuvwxyz"
    - constantes.majuscules qui correspond à "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    - constantes.chiffres   qui correspond à "0123456789"
    - constantes.speChars   qui correspond à "&~\"#'{([-|_\\^@)]=}$£%*!§/:;.,?<>"
    - constantes.lettres    qui correspond à constantes.minuscules + constantes.majuscules
    - constantes.normalPass qui correspond à constantes.lettres + constantes.chiffres
    - constantes.totalPass  qui correspond à constantes.normalPass + constantes.speChars
    - une liste des charactères que vous définissez de cette manière : "<votre liste de chars>" 
"""
typeOfChars = constantes.normalPass

"""
defauktSize définit le nombre de charactères par défaut que contiendra un password généré sans avoir remplit le champ prévut à cet effet.
Prend un entier.
"""
defaultSize = 8