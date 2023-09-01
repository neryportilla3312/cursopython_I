
#Primer modelo del clima  

constanteSolar = 1350 # se establece la constante solar 
albedoValor = 0.30    # se establece el albedo del planeta Tierra 
emisividadCuerpoNegro = 1  # se considera un cuerpo negro ideal, se considera el valor de epsilon 
constanteStefan = 5.67e-8  # se considera a la constante de stefan - boltzmann con notación cientifica 

t = (((constanteSolar)*(1-albedoValor))/(4*emisividadCuerpoNegro*constanteStefan))
# se debe de tener cuidado con la jerarquia de operaciones 
# la formula parte del balance de energía 

t2 = pow(t,1/4)    # parte de la formula de T a la cuarta potencia 


print("{0:.3f}".format(t2)+" K")












