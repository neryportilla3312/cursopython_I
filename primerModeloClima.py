
#Primer modelo del clima  

constanteSolar = 1350
albedoValor = 0.30
emisividadCuerpoNegro = 1 
constanteStefan = 5.67e-8

t = (((constanteSolar)*(1-albedoValor))/(4*emisividadCuerpoNegro*constanteStefan))

t2 = pow(t,1/4)

print("{0:.3f}".format(t2)+" K")












