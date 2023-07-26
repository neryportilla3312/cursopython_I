

#i > j 

#i >=j
#i < j 
#i <= j
#i ==j 
#i !=j 
 #if <condition>:
    #<expresion>
    #<expresion>   # el bloque de codigo está dentro de la sangria 
                  # por lo regular cuatro espacios son sangria 
# if <condition>:
  #  <expresion>
   # <expresion>
#else:
   # <expresion>
    #<expresion>

#how you denote blocks of code 


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








