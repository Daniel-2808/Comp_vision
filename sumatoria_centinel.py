print("Este programa captura importes")
info = """
     Este programa lleva el conteo de cuantos importes ha introducido un usuario.

     Va acumulando todos los importes que el usuario ingresa.

     SI el usuario desea terminar el programa, puede esctribir cualquier momento la palabra exit, quit, terminar.

                                                                    Elaborado por Daniel Rdz.


"""
print(info)
conteo = 0
suma = 0.0
mínimo = None
máximo = None

while True:
    user_massage = """
    Ingresa tu importe (MXN)
    Si quieres dejar de capturar importes puedes ingresar en cualquier momento exit, quit, terminar.
    """
    line = input("Ingresa tu importe(MXN)").lower()
    if line == "exit" or line == "quit" or line == "terminar":
        break
    try:
        value = float(line)
    except ValueError:
        print("Valor invalido. Intenta de nuevo (ej. 125.5)")

    conteo += 1 # Me dice cuantos numeros he ingresado
    suma += value # M e lleva la acumulación

    if mínimo is None or value < mínimo:
        mínimo = value

    if máximo is None or value > máximo:
        máximo = value

if conteo == 0:
    print("No se capturaron importes")
else:
    print("="*32)
    print(f"{conteo}")
    
                      

print("Programa finalizado")