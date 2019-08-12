#Auteur --> aiglematth
"""
Fichier de constantes
"""

##### CONSTANTES DE GENPASS.PY #####
minuscules = "abcdefghijklmnopqrstuvwxyz"
majuscules = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
chiffres   = "0123456789"
spechar    = "&~\"#'{([-|_\\^@)]=}$£%*!§/:;.,?<>"

lettres    = minuscules + majuscules
normalPass = lettres + chiffres
totalPass  = normalPass + spechar

##### CONSTANTES DE GUU.PY #####
geometry = "480x720"
intSize = (int(geometry.split("x")[0]), int(geometry.split("x")[1]))

title = "GenPass"