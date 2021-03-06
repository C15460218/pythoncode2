"""
Nombre: ventana.py
Objetivo: muestra como trabajar con ventanas gui en python y tkinter
Autor: Adrian Manuel Robles Jiménez
Fecha: 29 de julio de 2020
"""

# importar las librerias de tkinter
from tkinter import *
from tkinter import ttk

# Función para enviar mensaje al servidor
def sendToServer():
	print("Dato enviado ...")


# Función main
def main():
	# Creamos  la ventana contenedora
	win = Tk()
	# Modificamos parámetros de la ventana win
	win.geometry("400x400")
	win.title("Mi Primer Ventana en Python Tkinter")

       	# Creamos etiqueta
	label = ttk.Label(win, text="Texto a Enviar al Servidor").pack(side=TOP)
	txtCampo = ttk.Entry(win).pack(side=TOP)

	# Creamos un boton para enviar el contenido de la propiedad text del entry al servidor
	ttk.Button(win, text="Enviar  mensaje", command=sendToServer).pack(side=BOTTOM)    		

	# Creamos un boton y  lo colocamos en la ventana
	ttk.Button(win, text="Salir", command=quit).pack(side=BOTTOM)

  	# Ciclo para dibujar y esperar eventos 
	win.mainloop()





# para función main
if __name__ == "__main__":
	main()