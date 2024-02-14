def selecP(var):
    palabras = ["python", "programacion", "computadora", "desarrollo", "inteligencia"]
    return palabras[var]
#se define la seleccion de palabras 
def imprimirAhorcado(parametro_intentos):
    if parametro_intentos == 1:
        print("""
                       ___
                      |   |
                     _O/  |
                      |   |
                     / \  |
                    ______|
        """)
    elif parametro_intentos == 2:
        print("""
                       ___
                      |   |
                     _O/  |
                      |   |
                       \  |
                    ______|
        """)
    elif parametro_intentos == 3:
        print("""
                       ___
                      |   |
                     _O/  |
                      |   |
                          |
                    ______|
        """)
    elif parametro_intentos == 4:
        print("""
                       ___
                      |   |
                     _O/  |
                          |
                          |
                    ______|
        """)
    elif parametro_intentos == 5:
        print("""
                       ___
                      |   |
                      O/  |
                          |
                          |
                    ______|
        """)
    elif parametro_intentos == 6:
        print("""
                       ___
                      |   |
                      O   |
                          |
                          |
                    ______|
        """)
# se definio la estructura de los fallos 
print("¡Bienvenido al juego del ahorcado!")

palabra = selecP(3)
intentosF = 6
letrasCo = []
# aca se puso los parametros para el juego 
while intentosF > 0 and set(letrasCo) != set(palabra):
    letra = input("Ingrese letra: ")
#aca se coloco la condicion para saber si lo q se ingresa en una caracter y no un numero 
    if letra.isalpha():
        if letra in letrasCo:#de aca
            print("Ya has ingresado esta letra antes.")
        elif letra in palabra:
            letrasCo.append(letra)
            print("¡Correcto! La letra está en la palabra.")
        else:
            intentosF -= 1
            print(f"Letra fallida. Te quedan {intentosF} intentos.")
            print("Letras adivinadas:", letrasCo)
            imprimirAhorcado(intentosF) #hasta aca se condiciona la letra de la palabra 
    else:
        print("Caracter no válido. Ingrese una letra.")
#y aca se condiciona la letra como caracter 
if set(letrasCo) == set(palabra):
    print("¡Felicidades! Has adivinado la palabra:", palabra)
else:
    print("Fin del juego. La palabra correcta era:", palabra)
