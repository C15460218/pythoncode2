"""
Nombre: cliente.py
Objetivo: implementa un cliente con socket
Autor: tomado de https://realpython.com/python-sockets/
04/08/2020
"""

#!/usr/bin/env python3

import socket

HOST = '192.168.0.102'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b'Hola Mundo Peludo')
    data = s.recv(1024)



# Función main
def main():
	# Creamos  la ventana contenedora
	win = Tk()
	# Modificamos parámetros de la ventana win
	win.geometry("400x400")
	win.title("Cliente Socket")

       	# Creamos etiqueta
	label = ttk.Label(win, text="Texto a Enviar al Servidor").pack(side=TOP)
	txtCampo = ttk.Entry(win).pack(side=TOP)
	label2 = ttk.Label(win, text="Texto Recibido del servidor:\n").pack(side=TOP)
	label3 = ttk.Label(win, text=('Received', repr(data)).pack(side=TOP)

	# Creamos un boton para enviar el contenido de la propiedad text del entry al servidor
	ttk.Button(win, text="Enviar  mensaje", command=sendToServer).pack(side=BOTTOM)    		

	# Creamos un boton y  lo colocamos en la ventana
	ttk.Button(win, text="Salir", command=quit).pack(side=BOTTOM)

  	# Ciclo para dibujar y esperar eventos 
	win.mainloop()





# para función main
if __name__ == "__main__":
	main()