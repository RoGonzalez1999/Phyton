funcionando = True

while funcionando == True:
    #se imprime un menú de opciones para que el usuario elija
    print ("=============================")
    print ("1 - Alta de alumno")
    print ("2 - Baja de alumno")
    print ("3 - Modificación de datos")
    print ("4- Salir")
    print ("=============================")
    print ()

    #Acá se ejecuta algo según la opción que se elija del menú
    seleccion = input ("Ingrese la opción deseada: ")
    if seleccion == "1":
        nombre = input ("Ingrese el nombre del alumno nuevo: ")
        dni = input ("Ingrese el DNI: ")
        fecha = input ("Ingrese la fecha de nacimiento: ")
    elif seleccion == "2":
        nombre_sacar = input ("Ingrese el nombre del alumno a dar de baja: ")
    elif seleccion == "3":
        nombre_mod = input ("Ingrese el nombre del alumno a modificar: ")
    elif seleccion == "4":
        funcionando = False

#Aca se cierra el programa
        print ()
        print ("Salio del programa")
