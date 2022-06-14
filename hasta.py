funcionando = True

#TODO LO QUE SIGUE SE EJECUTA SOLAMENTE SI FUNCIONANDO ES VERDADERO
while funcionando == True:
    base = int(input ("Ingrese la base del rectángulo: "))
    altura = int(input ("Ingrese la altura del rectángulo: "))
    superficie = base * altura
    print (f" La superficie de este rectángulo es {superficie}")
    print ()

    #Pregunta si queremos seguir calculando
    seguir = input ("Quiere seguir calculando? S/N: ")
    if seguir == "N":
        funcionando = False

#Esto se ejecuta solamente cuando no se quiere calcular más
print ("El programa ha terminado.")
