#string 
hi = "hello there" # objeto string 
#concatenate string 
name = " ana"
greet = "hi" + name
# se concatena con el operador de asignacion 
# el operador concatenacion no agrega espacios implicitamente 
greeting = hi + " " + name
print(greet)
print(greeting)

#operador multiplicacion , operador estrella 
# repetir esa cadena n veces 
#cuidado al multiplicar dentro de los parentesis 
saludo = "hola"
name = "pablo"
frase = "recuerda no tirar basura"
oracion = (saludo + " " +name + " "+frase+ " ")*5
print(oracion)

x = 10
print(x)
x_str = str(x) # se convierten en objetos cadena 
print("mi número favorito es", x, ".", "x = ", x)
# se agrega un espacio automaticamente
print("mi número favorito es" + x_str + " . " + "x = " + x_str)

text = input("Escribe algo...")
print(5*text)

num = int(input("Escribe algo"))
# cast para convertir a un número y poder realizar operaciones 

print(5*num)

# el texto ingresado por el usuario se convierte en una cadena 