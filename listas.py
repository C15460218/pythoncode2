"""
Nombre: listas.py
Objetivo: muestrala funciòn de las listas en python
Autor: Adrian Manuel Robles Jimènez
Fecha: 04/08/2020
"""


def main():
    # Una lista es una estructura de datos en python
    # La ventaja aceptan datos de tipos distintos
    # Creamos una lista
    lista = [1, 23.01, False, "hola lista", 'A', [-1,-5, "hola", 0.0], -12, 'A']
    # Lista Vacia
    listaVacia = []
    # Accesando elementos de la lista
    for elemento in lista:
        print("El elemento de la lista es: ",elemento)
    for i in listaVacia:
        print("El elemento de la lista es: ",i)
    #imprimir un elemento de la lista
    print("elemento en la posicion 3: ",lista[3])
    print("elemento en la posicion -5: ",lista[-5])
    print(lista[-2])
    print(lista[5])
    # leer el elemento que esta en la posicion 2 de la lista interna
    print(lista[5][2])
    # Métodos de las listas
    lista.append("El maestro no sabe...")
    for element in lista:
        print("El elemento de la lista es: ",element)
    # count regresa el nimero de veces que se repite un numero en la lista
    print("Elemento se repite: ",lista.count("pelochas"))
    #index() imprime el indice de un elemento en la lista
    print("La posicion de False es: ", lista.index(False))
    # eliminar elementos de la lista : remove()
    lista.remove("hola lista")
    for x in lista:
        print("El elemento de la lista es: ",x)




if __name__ == "__main__":
    main()