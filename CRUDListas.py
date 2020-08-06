"""
Nombre: CRUDLista.py
Objetivo: implementa las funciones crud en una lista en python
Autor: Adrian Manuel Robles Jiménez
Fecha: 4 de agosto de 2020
"""

#Declaramos una lista como variable global
lista = []

#Agregar Elemento a la lista
def addElement():
    print("== Agregar Elemento ==")
    e = input("Ingresa elemento: ")
    lista.append(e)
    print("Elemento ", e, " agregado")
    return



#Mostrar elemento de la lista
def getElement():
    print("Show")



#Función para modificar elemento de la lista
def modifyElement():
    print("Modify")




#Eliminar elemento de la lista
def delElement():
    print("Delete")



def dashboard():
    print("== Operaciones CRUD con Lista en Python ==")
    print("1.- Agregar elementos")
    print("2.- Buscar elementos")
    print("3.- Cambiar elementos")
    print("4.- Eliminar elementos")
    print("5.- Imprimir elementos")
    print("6.- Salir")


def main():
    ciclo= 'S'
    while ciclo == 'S' or ciclo == 's':
        dashboard()
        ciclo = input("Seleccione una opcion entre 1 y 5: ")
        if ciclo == 1:
            #Incovar función para agregar elemento
            addElement()
        

    else:
        print("*** Fin del programa")



if __name__ == "__main__":
    main()