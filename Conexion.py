# -*- coding: utf-8 -*-

import pyodbc #Instalar con pip

class Conexion:
    def __init__(self):
        #obvio que se debe de guardar esto en una variable de entorno
        self.driver = "Microsoft Access Driver (*.mdb, *.accdb)"
        self.path = r".\database\Tienda.accdb"
        self.conn = None
        self.cursor = None
    
    def conectar(self):
        self.conn = pyodbc.connect(driver = self.driver, dbq = self.path)
        self.cursor = self.conn.cursor()
       
    def desconectar(self):
        if self.cursor != None or self.conn != None:
            self.cursor.close()
            self.conn.close()
        else:
            pass
