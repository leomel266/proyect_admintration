import sqlite3
from tkinter import messagebox
import os

ruta = os.path.dirname(os.path.abspath(__file__))+"\\log.txt"
class Errorcon:
    def errorconectar():
        log = open(ruta, 'a')
        print("Error al conectarse con la base de datos", file=log)

class Crud:
    def __init__(self, ):
        self.conectar()
        try:
            self.micursor.execute('''CREATE TABLE registros( 
            ID integer PRIMARY KEY AUTOINCREMENT, 
            PRODUCTO VARCHAR(50),
            CATEGORIA VARCHAR(50),
            CANTIDAD INTEGER(4),
            UNIDAD INTEGER(4),
            UBICACION VARCHAR(50))''' )
            messagebox.showinfo("Productos", "Base creada con éxito")
        
        except:
            Errorcon.errorconectar() 

        finally:
            pass


    def conectar(self):
        self.miconexion = sqlite3.connect("productos.db")
        self.micursor = self.miconexion.cursor()
        return self.micursor, self.miconexion


    def alta(self, nombre, categoria, cantidad, unidad, ubicacion):
        self.conectar()
        datos = (
                nombre,
                categoria,
                cantidad,
                unidad,
                ubicacion
        )
        #check(datos)
        self.micursor.execute("INSERT INTO registros VALUES(NULL, ?, ?, ?, ?, ?)",
                        (datos)
        )
        self.miconexion.commit()
        self.miconexion.close()
        print("Registro ingresado")
        


    def baja(self, id):
        self.conectar()
        self.micursor.execute("DELETE FROM registros WHERE ID=?", (id,))
        self.miconexion.commit()
        print("Registro borrado")
        

    def modificar(self, nombre, categoria, cantidad, unidad, ubicacion, id):
        self.conectar() 
        self.micursor.execute("""UPDATE registros SET 
                        PRODUCTO = :prod,
                        CATEGORIA = :categ,
                        CANTIDAD = :cant,
                        UNIDAD = :unid,
                        UBICACION = :ubic
                        WHERE ID = :oid""",
                        {
                        'prod':nombre,
                        'categ':categoria,
                        'cant':cantidad,
                        'unid':unidad,
                        'ubic':ubicacion,
                        'oid':id                
                        }
        )              
            
        self.miconexion.commit()
        self.miconexion.close()
        print("Registro modificado")
        

    def consulta(self, id, categoria):
        self.conectar()
        datos = self.micursor.execute("SELECT * FROM registros WHERE ID =? or CATEGORIA like ?", (id, categoria,))
        data = list(datos.fetchall())   
        self.miconexion.commit()
        self.miconexion.close()
        return data


    def selectall(self):
        self.conectar()
        todo = self.micursor.execute("SELECT * FROM registros")
        self.miconexion.commit()
        return todo




