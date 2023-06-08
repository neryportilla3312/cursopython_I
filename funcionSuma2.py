

def puntuacion(clase):
    return sum(clase) / len(clase)



clase = [9,4,7]
media = puntuacion(clase)
print("La puntuacion de la primera clase es: ", media)


clase = [9,4,5,6,7]
media = puntuacion(clase)
print("La puntuacion de la segunda clase es: ", media)