import tse as fn
letrasProposicionalesA = ['p', 'q', 'r', 's', 't']
# # Formula a la cual encontrar su forma clausal
formula = "(p>q)"

# Aplicando el algoritmo de Tseitin a formula
# Se obtiene una cada que representa la formula en FNC
fFNC = fn.Tseitin(formula, letrasProposicionalesA)

# Se obtiene la forma clausal como lista de listas de literales
fClaus = fn.formaClausal(fFNC)

# Imprime el resultado en consola
print(fClaus)
#nombre de los integrantes:
    #ANDREY LIZARAZO
    #FELIPE FLORIÁN
