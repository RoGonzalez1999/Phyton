#Ojo, tengo que poner el int adelante porque
# el input siempre me devuelve un string
#y no puedo usarlo como número







edad = int(input ("Ingrese su edad: "))

#Ahora que ya pasé la edad a número
#valido la entrada al local

if edad > 17:
    print ("Puede entrar")
elif edad > 15 and edad < 18:
    print ("Puede entrar con un adulto responsable")
elif edad < 16:
    print ("No se permite el ingreso")
else:
    print ("Se ha ingresado mal la edad")
