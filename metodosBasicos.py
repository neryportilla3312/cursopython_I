#strip / se pueden remover caracteres seleccionados 

txt = "  hola mundo" 
txt1 = "hola mundo ***"
txt2 = "hola mundo"





txt1 = txt1.strip("*")
txt2 = txt2.strip(",")



print(txt)
print(txt1)
print(txt2)

# lstrip  / remueve espacios vacios a la izquierda de la cadena

cadena = "      hola a todos "
cadena = cadena.lstrip()
print(cadena)

# rstrip / remueve espacios a la derecha de la cadena 

cad = "hola     a      todos      "
cad = cad.rstrip()
print(cad)



# split  / devuelve una lista de palabras o tokens usando sep como separacion 
# separa una cadena en partes 

oracion = "hola a todas las personas"
oracion = oracion.split()
print(oracion)

frase = "cada persona tiene su forma de amar"
frase = frase.split()
print(frase)

# startswith   / valida el comienzo de una cadena / devuelve cierto o falso 

a = "www tik tok"
a = a.startswith("w")
print(a)


# upper   / convierte a mayusculas, los numeros son ignorados

minusculas = "14 de diciembre del 2002"
min = minusculas.upper()
print(min)

# find / retorna un entero que es la posicion de donde se encuentra 
# si no se encuentra la subcadena retorna -1
texto = "vamos a jugar uno con uno de mis amigos"
print(texto.find("os"))

print(texto.find("os")) #nueva linea de texto



#index 
# que posicion ocupa la palabra ave en la lista index
animales = ['perro','ave','ave']
index = animales.index('perro')
print(index)





