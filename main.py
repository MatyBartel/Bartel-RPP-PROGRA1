from Funcion1 import aplicarAumento
from Funcion2 import reemplazarCaractres
from Funcion3 import ordenarCaracteres
import os

# Matias Bartel RPP Programacion I

os.system("cls")

aplicarAumento(20)

caracter_a_reemplazar = "o"
caracter_nuevo = "u"
nueva_cadena,reemplazos = reemplazarCaractres("Hola Mundo",caracter_a_reemplazar,caracter_nuevo)

print("La nueva cadena es:",nueva_cadena," - Se reemplazo \"",caracter_a_reemplazar,"\" por  \"",caracter_nuevo,"\"  una cantidad de veces de: ",reemplazos)

ordenarCaracteres("algoritmo")