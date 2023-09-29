# 15 # Dada la tupla #1 de resources.py, pedir al usuario que ingrese un nombre de una ciudad,
# devolver si se encuentra en la primer o segunda mitad de la tupla, según el indice que define su posición.
# Si se encuentra exactamente en el medio, imprimir {"Se encuentra en el medio de la tupla"}
# Si la ciudad no se encuentra en el listado, imprimir {"No se encuentra {nombre ciudad} en la lista"}

ciudades = ("San Jorge", "Quitilipi", "Granadero Baigorria", "Alderetes", "Gualeguay", "Chimbas", "Rada Tilly", "Cote-Lai", "Elena", "Yerba Buena", "Laboulaye", "La Rioja", "Castelli", "Aminga", "Isla Verde", "Pirane", "General Enrique Godoy", "Alumine", "Rio Pico", "Sampacho", "Villa de Soto", "Embarcacion", "Caseros", "Jesus Maria", "Salta",
            "Esquina",
            "Puerto Iguazu", "Mercedes", "Castelli", "Cinco Saltos", "El Bolson", "Tamberias", "Guernica", "Doblas", "Villa Santa Rita", "Mercedes", "Carlos Casares", "Vera", "Zapala", "Santa Ana", "Libertador General San Martin", "Villa Maria", "Basail", "Gualeguay", "Villa La Angostura", "Basail", "San Lorenzo", "Tostado", "Libertad", "General Conesa", "General Pico")

longitud = len(ciudades)

if longitud%2 == 0:
    print("Lista impar!")


ciudad = input("Dime una ciudad:\n")

posicion = ciudades.index(ciudad)

if posicion < (longitud-1)/2:
    print ("Esta en la primera mitad")
elif posicion > (longitud-1)/2:
    print("Esta en la segunda mitad")
else:
    print("La ciudad está en el medio")