from tkinter import ttk
from tkinter import *

import sqlite3

class Producto:
    dbnombre = 'basedatos.db'
    def __init__(self, window):
        self.wind = window
        self.wind.title("Aplicacion de productos")
    
##a el atributo frame se le da el label frame, grid posiciona los objetos dentro de la ventana
##sticky da a recorrer las posiciones de este a oeste en toda la ventana
        #contenedor
        frame = LabelFrame(self.wind, text="Registra un nuevo producto")
        frame.grid(row=0, column = 0, columnspan=3, pady = 20)

        #Entrada del nombre
        Label(frame, text="Nombre: ").grid(row=1, column=0)
        self.nombre = Entry(frame)
        #le da el cursos automatico a el input nombre
        self.nombre.focus()
        self.nombre.grid(row=1, column=1)

        #Entrada del precio
        Label(frame, text="Precio: ").grid(row=2, column=0)
        self.precio = Entry(frame)
        self.precio.grid(row=2, column=1)

        #Boton de agregar producto
        ttk.Button(frame, text="Guardar producto").grid(row=3, columnspan=2, sticky= W + E)

        #Tabla
        self.tree = ttk.Treeview(height= 10, columns = 2)
        self.tree.grid(row=4, column= 0, columnspan = 2)
        self.tree.heading('#0', text ="Nombre", anchor=CENTER)
        self.tree.heading("#1", text="Precio ", anchor=CENTER)

        self.get_productos()

    def run_query(self, query, parametros=()):
        with sqlite3.connect(self.dbnombre) as conn:
            cursor = conn.cursor()
            result = cursor.execute(query, parametros)
            conn.commit()
        return result
    def get_productos(self):
        #limpiando tabla
        elementos = self.tree.get_children()
        for element in elementos:
            self.tree.delete(element)
            #consultando los datos
        query ='SELECT * FROM Productos ORDER BY nombre DESC'
        db_rows = self.run_query(query)
        for row in db_rows:
            self.tree.insert('', 0, text = row[1], values = row[2])

if __name__=='__main__':
   window = Tk()
   Producto(window)
   window.mainloop()




