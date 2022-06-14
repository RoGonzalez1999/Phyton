edad = int(input("Introduce tu edad: "))
# Se decide el precio según la edad
if edad < 4:
    precio = 0
elif edad <= 18:
    precio = 5000
else:
    precio = 3000
# Mostrar precio
print("El precio de la entrada es", precio, "$.")
