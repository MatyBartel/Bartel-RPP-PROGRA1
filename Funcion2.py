# Matias Bartel RPP Programacion I
#2. Crear una función que se llame reemplazarCaracteres que reciba una cadena de caracteres como primer parámetro, 
# un carácter como segundo y otro carácter  como tercero,  la misma deberá reemplazar cada ocurrencia del segundo parámetro 
# por el tercero y devolver la cantidad de veces que se reemplazo ese carácter  en la cadena.

def reemplazarCaractres(cadena:str,caracter_a_reemplazar:str,caracter_nuevo:str):
    """
    Function: Recibe por parametro una cadena, un caracter y un segundo caracter. Reemplazara en la cadena ingresada, el primer caracter por el segundo.

    Args:
        cadena (str): Cadena que vamos a querer usar.
        caracter (str): Caracter que queremos reemplazar.
        caracter_reemplazo (str): Caracter que reemplazaremos por el 1ro.
    
    Returns:
        nueva_cadena (str): Sera la nueva cadena con sus caracteres remplazados.
        reemplazos (int): Cantidad de reemplazos que se hicieron.

    """

    nueva_cadena = ""
    reemplazos=0
    for caracter in cadena:
        if caracter == caracter_a_reemplazar:
            nueva_cadena += caracter_nuevo
            reemplazos+= 1
        else:
            nueva_cadena += caracter
    return nueva_cadena,reemplazos