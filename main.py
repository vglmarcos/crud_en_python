# -*- coding: utf-8 -*-

#Toda libreria que importe se debe de instalar con pip desde el cmd, no sea flojo
#aun asi abajo deje instrucciones mas detalladas
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
from Conexion import Conexion

class Login:
    def __init__(self, window, title):
        self.window = window
        self.w = 400
        self.h = 400
        self.x = int(self.window.winfo_screenwidth() / 2 - self.w / 2)
        self.y = int(self.window.winfo_screenheight() / 2 - self.h / 2)
        self.window.title(title)
        self.window.geometry(f"{self.w}x{self.h}+{self.x}+{self.y}")
        self.window.configure(background = '#ffffff')
        self.window.iconbitmap('./images/codigo.ico')

        #user y pass para el login
        self.user = "a"
        self.password = "a"

        self.estilo_img = ImageTk.PhotoImage(Image.open("./images/login.png"))
        self.estilo = Label(self.window, image = self.estilo_img,
                                  background = "#ffffff", borderwidth = 0, highlightthickness = 0)
        self.estilo.place(x = 0, y = 0)

        self.texto = Label(self.window, text = "Iniciar sesión", background = "#fcba03", foreground = "#ffffff",
                            font = ("Tahoma", 24))
        self.texto.place(x = 40, y = 40)

        self.usuario = Label(self.window, text = "Usuario", background = "#ffffff", foreground = "#fcba03", 
                                font = ("Tahoma", 16))
        self.usuario.place(x = 30, y = 150)

        self.usuarioIn = Entry(self.window, width = 20, font = ("Tahoma", 16),
                              background = "#f4f4f4", foreground = "#fcba03")
        self.usuarioIn.place(x = 150, y = 155)
        self.usuarioIn.bind("<Key>", self.keyPressed)
        self.usuarioIn.bind("<FocusIn>", self.focus)
        self.usuarioIn.bind("<FocusOut>", self.noFocus)

        self.contra = Label(self.window, text = "Contraseña", background = "#ffffff", foreground = "#fcba03", 
                                font = ("Tahoma", 16))
        self.contra.place(x = 30, y = 200)

        self.contraIn = Entry(self.window, width = 20, font = ("Tahoma", 16), show = "•",
                              background = "#f4f4f4", foreground = "#fcba03")
        self.contraIn.place(x = 150, y = 205)
        self.contraIn.bind("<Key>", self.keyPressed)
        self.contraIn.bind("<FocusIn>", self.focus)
        self.contraIn.bind("<FocusOut>", self.noFocus)

        self.ingresar = Button(self.window, text = "Ingresar", command = self.ingreso, font = ("Tahoma", 14), 
                                background = "#f4f4f4", foreground = "#fcba03", width = 10, borderwidth = 2, 
                                highlightthickness = 1, activeforeground = "#ffffff", activebackground = "#fcba03")
        self.ingresar.place(x = 200, y = 280)
        self.ingresar.bind("<Key>", self.keyPressed)
        self.ingresar.bind("<FocusIn>", self.focus)
        self.ingresar.bind("<FocusOut>", self.noFocus)
    
    def ingreso(self):
        '''Ingresar al sistema.'''
        if self.usuarioIn.get().strip() != "" and self.contraIn.get() != "":
            if self.user == self.usuarioIn.get().strip() and self.password == self.contraIn.get():
                messagebox.showinfo("Bienvenida", f"Bienvenido, {self.usuarioIn.get().strip()}.")
                self.window.destroy()
                window = Tk()
                menu = Menu(window, "Menú")
                window.mainloop()
            else:
                messagebox.showinfo("Error", "Usuario o contraseña incorrectos.")
        else:
            messagebox.showinfo("Error", "Se deben llenar todos los campos.")
    
    def keyPressed(self, event):
        '''Evento que controla el comportamiento del keyboard'''
        if event.char == "\r":
            if self.usuarioIn.get().strip() != "" and self.contraIn.get() != "":
                if self.user == self.usuarioIn.get().strip() and self.password == self.contraIn.get():
                    messagebox.showinfo("Bienvenida", f"Bienvenido, {self.usuarioIn.get().strip()}.")
                    self.window.destroy()
                    window = Tk()
                    menu = Menu(window, "Menú")
                    window.mainloop()
                else:
                    messagebox.showinfo("Error", "Usuario o contraseña incorrectos.")
            else:
                messagebox.showinfo("Error", "Se deben llenar todos los campos.")
        else:
            pass

    def focus(self, event):
        '''Evento que controla si un componente esta siendo enfocado.'''
        if event.widget == self.ingresar:
            self.ingresar.configure(state = "active")
        else:
            event.widget.configure(background = "#fcba03", foreground = "#ffffff")

    def noFocus(self, event):
        '''Evento que controla si un componente deja de ser enfocado.'''
        if event.widget == self.ingresar:
            self.ingresar.configure(state = "normal")
        else:
            event.widget.configure(background = "#f4f4f4", foreground = "#fcba03")

class Menu:
    def __init__(self, window, title):
        self.window = window
        self.w = 400
        self.h = 400
        self.x = int(self.window.winfo_screenwidth() / 2 - self.w / 2)
        self.y = int(self.window.winfo_screenheight() / 2 - self.h / 2)

        self.db = Conexion() 
        try: #intentamos conectarnos a la db
            self.db.conectar()
            print("Se ha conectado a la base de datos.")
            resultados = [list(i) for i in self.db.cursor.execute("SELECT * FROM Producto").fetchall()]
            for i in resultados:
                print(i)
        except:
            print("Error al conectar")

        self.window.title(title)
        self.window.geometry(f"{self.w}x{self.h}+{self.x}+{self.y}")
        self.window.configure(background = '#ffffff')
        self.window.iconbitmap('./images/codigo.ico')

        self.estilo_img = ImageTk.PhotoImage(Image.open("./images/login.png"))
        self.estilo = Label(self.window, image = self.estilo_img,
                                  background = "#ffffff", borderwidth = 0, highlightthickness = 0)
        self.estilo.place(x = 0, y = 0)

        self.salir = Button(self.window, text = "Salir", command = self.exit, font = ("Tahoma", 14), background = "#f4f4f4",
                            foreground = "#fcba03", width = 6, borderwidth = 2, highlightthickness = 1,
                            activeforeground = "#ffffff", activebackground = "#fcba03")
        self.salir.place(x = 300, y = 50)
        self.salir.bind("<Key>", self.keyPressed)
        self.salir.bind("<FocusIn>", self.focus)
        self.salir.bind("<FocusOut>", self.noFocus)
    
    def exit(self):
        '''Salir del sistema.'''
        print("Se ha desconectado de la base de datos.")
        self.db.desconectar()
        self.window.destroy()
        window = Tk()
        login = Login(window, "Ingresar")
        window.mainloop()
    
    def keyPressed(self, event):
        '''Evento que controla el comportamiento del keyboard'''
        if event.char == "\r":
            self.window.destroy()
            window = Tk()
            login = Login(window, "Ingresar")
            window.mainloop()
        else:
            pass
    
    def focus(self, event):
        '''Evento que controla si un componente esta siendo enfocado.'''
        if event.widget == self.salir:
            self.salir.configure(state = "active")
        else:
            pass

    def noFocus(self, event):
        '''Evento que controla si un componente deja de ser enfocado.'''
        if event.widget == self.salir:
            self.salir.configure(state = "normal")
        else:
            pass
        

if __name__ == "__main__":
    window = Tk()
    login = Login(window, "Ingresar")
    window.mainloop()

#--------------------------------------Instrucciones--------------------------------------------------------------

#Ejemplos con el cursor: 
#usar el cursor para obtener las categorias de la tabla Producto
#categorias = [x for i in self.db.cursor.execute("SELECT DISTINCT cat_prod FROM Producto").fetchall() for x in i]
#usar el cursor para consultar toda la tabla Producto
#resultados = [list(i) for i in self.db.cursor.execute("SELECT * FROM Producto").fetchall()]
#for i in resultados:
#    print(i)

#Instalar la libreria pyodbc con 'pip install pyodbc' para la conexion a la db
