#comentarios primer modelo

constanteSolar = 1350       #valor de la constante solar 

albedoValor = 0.30          #valor promedio del albedo planetario en la Tierra 

emisividadCuerpoNegro = 1   #valor de la emisividad de cuerpo negro
# la mayoria de la materia condensada tiene un valor cerecano a 1 
# toma en cuenta que no existe un cuerpo negro en la realidad, solo en la teoría 

constanteStefan = 5.67e-8   # valor de la constante de Stefan - Boltzmann 

# ten cuidado que el valor de las unidades sea el adecuado 

t = (((constanteSolar)*(1-albedoValor))/(4*emisividadCuerpoNegro*constanteStefan))

# se realiza la división por separado, aunque puedes unir toda la expresión en una sola

t2 = pow(t,1/4)

# se obtiene el valor de la raíz cuarta 

# se imprime el resultado limitando el número de decimales
print("El valor de la temperatura es de: " + "{0:.3f}".format(t2)+" K")
