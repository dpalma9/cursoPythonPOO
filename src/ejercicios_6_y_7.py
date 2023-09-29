"""
# 7 # Dada la lista [5, 7, 3, 0, 4, 0, 4, 3, 4, 8, 6, 9, 8, 5, 1, 2, 3, 9, 7, 2, 1, 6] # pedir al usuario que ingrese un número entre 0 y 9 y devolver:# - cuantas veces aparece el número en la lista# - el indice de la segunda vez que aparece en la lista (suponer q aparece dos veces)
"""

lista = [5, 7, 3, 0, 4, 0, 4, 3, 4, 8, 6, 9, 8, 5, 1, 2, 3, 9, 7, 2, 1, 6]

numero = input("Que numero quieres buscar:\n")

#print("Numero --> " + numero)
print(lista.count(int(numero)))
#print(lista.count(5))

print(lista.index(int(numero)))
