"""
Nombre: diccionario.py
Objetivo: muestra la operaciòn de los diccionarios en python
Autor: Adrian Manuel Robles Jiménez
Fecha: 5 de agosto de 2020
"""

# un diccionario es una estructura de datos que almacena valore heterogeneos
# pero los almacena en un formato de clave:valor. Quiere decir que cada elemento
# en el diccionario se almacena como una lista de pares key:valor
# Por ejemplo: 'nombre':'Francisco Cervantes Zambrano'
# No son mutables, it does mean no cambian. Una vez que los creamos permanecerán
# con los mismos valores, no podremos introducir más datos

def main():
    # Creamos un diccionario con distintos keys y datos
    dic = {'clave': 20082133,'nombre':'Erick José Verduzco Campos', 'edad':54,'cursos':['Python','Progra Web','Inteligencia Artificial']}
    # Listar items del diccionario
    print("Los items del son: ",dic)
    # IMprimir un item de un diccionario proporcionando su key
    print("El valor de la key es: ", dic['nombre'],"\n")
    #Imprimir los valores de todos los keys del diccionario
    for i in dic:
        print(i,":",dic[i])
    print("\n")
    #En el caso de la lista uncluida como un item del diccionario, lo accesamos
    print(dic['cursos'][2])
    print("\n")
    for x in dic['cursos']:
        print(x)
    print("\n")
    #Investigar los métodos de los diccionarios y correrlos en el programa
    # get, pop, key, clean, items, update




if __name__ == "__main__":
    main()