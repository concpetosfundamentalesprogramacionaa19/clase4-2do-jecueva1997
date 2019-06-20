"""
    @jecueva1997
    Manejo de estructuras
"""
# Mi nombre es: Jeferson y mi apellido es: Cueva
# contiene llaves
diccionario = {"nombre": "Jeferson", "apellido": "Cueva"}
diccionario2 = {"nombre": "Luis", "apellido": "Alvares"}

lista = [diccionario, diccionario2]
print("Imprimir diccionario")
for l in lista:
	midiccionario = l
	print("Mi nombre es: %s y mi apellido es: %s" % \
    		(midiccionario["nombre"], \
    			midiccionario["apellido"])
    	)


