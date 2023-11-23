

#cadena de texto
print("mensaje")



#suma de numeros 
a = 4 
b = 3
c = a+b
print(c)


#stefanBoltzman
albedo = 0.33
consSolar = 1350
blackBody = 0.99
consStefan = 5.67e-8
t = (((consSolar)*(1-albedo))/(4*blackBody*consStefan))
t2 = pow(t,1/4)
print("temp: " + "{0:.3f}".format(t2)+" K")



#condicionales
x = float(input("Ingrese un numero x: "))
y = float(input("Ingrese un numero y: "))

if x == y:
    print("Los numeros son iguales")
    if y != 0:
        print("por lo tanto, x /y es", x / y)

elif x < y: 
    print("x es mas chico")

else:
    print("y es mas chico")

print("gracias!")

#ciclo for
numeros = [10,15,200,2]
for i in numeros:
print(i)








