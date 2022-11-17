from tkinter import *
from tkinter import messagebox

#-------------------
#funciones de la app
#-------------------

def SUMAR ():
    z=pow(int(n.get()),1/int(a.get()))
    t_resultado.insert(INSERT, " Resultados:\n La raiz es  "+str(z)+"\n")

def borrar ():
    messagebox.showinfo("Suma 1.0", " Los datos seran borrados...")
    X.set("")
    n.set("")
    t_resultado.delete("1.0","end")
    
def salir():
     messagebox.showinfo("Suma 1.0", "La app se cerrara...") 
     ventana_principal.destroy()

ventana_principal=Tk()

#titulo de la ventana 
ventana_principal.title("RAIZ CUADRATICA")

# establecer tamaño de la ventana 
ventana_principal.geometry("800x500")

# deshabilitar boton de maximar
ventana_principal.resizable(0,0)

#color de fondo de la ventana principal
ventana_principal.config(bg="black")

#--------------------
# variables globales
#--------------------

a= StringVar()
n= StringVar()
z= IntVar()

#-----------------
# frame entrada
#-----------------

frame_entrada = Frame(ventana_principal )
frame_entrada.config (bg="azure4", width=780, height=240)
frame_entrada.place(x=10,y=10)

#Etiqueta para el titulo de la app
titulo= Label(frame_entrada, text="Colegio San Jose de Guanenta")
titulo.config(bg="azure4", fg="yellow" , font=("Arial", 16))
titulo.place(x=320, y=10)

# Etiqueta para el subtitulo de la app
subtitulo = Label(frame_entrada, text ="Especialidad de sistemas")
subtitulo.config(bg="azure4", fg="blue", font=("Arial", 15))
subtitulo.place(x=320, y=30)

#Etiqueta para el subtitulo2 de la app
subtitulo2 =Label(frame_entrada, text="Hallar la Raiz Cuadratica")
subtitulo2.config(bg="azure4", fg="black", font=("Arial", 12), anchor=CENTER)
subtitulo2.place(x=350, y=70)

# imagen - logo de la app 
logo = PhotoImage(file = "img/logo_EcuacionCuadratica.png")
etiq_logo = Label (frame_entrada,image=logo)
etiq_logo.place(x=10, y=10)

#Etiqueta para valor a
etiq_z = Label(frame_entrada, text="valor de a = ")
etiq_z .config(bg="ivory2", fg="blue", font=("Arial", 15), anchor=CENTER)
etiq_z.place(x=350, y=100)

#Entry para valor a
entry_a = Entry(frame_entrada,width=4, textvariable=a)
entry_a .config(font=("Arial", 20), justify=CENTER)
entry_a .focus_set()
entry_a.place(x=560, y=150)

#Etiqueta para valor b
etiq_a = Label(frame_entrada, text="valor de a = ")
etiq_a.config(bg="ivory2", fg="blue", font=("Arial", 15), anchor=CENTER)
etiq_a.place(x=350, y=160)

#Entry para valor b
entry_n = Entry(frame_entrada)
entry_n .config(font=("Arial", 20),width=4, textvariable=n)
entry_n .config(font=("Arial", 20))
entry_n.place(x=550, y=100)
"""
#-----------------
# frame operaciones
#-----------------

frame_operaciones = Frame(ventana_principal )
frame_operaciones.config (bg="NavajoWhite2", width=780, height=150)
frame_operaciones.place(x=10,y=250)

#boton para calcular el iva - texto
bt_sum= PhotoImage("img/Engranaje.png")
bt_sumar= Button(frame_operaciones, image=bt_sum, width=120, height=125, command=SUMAR)
bt_sumar.place(x=100, y=5)


bt_bor= PhotoImage(file="img/boton_borrar.png")
bt_borrar= Button(frame_operaciones, image=bt_bor, width=125, height=120, command=borrar)
bt_borrar.place(x=330, y=7)


bt_sal= PhotoImage(file="img/boton_salir.png")
bt_salir= Button(frame_operaciones, image=bt_sal, width=125, height=120, command=salir)
bt_salir.place(x=585, y=7)

#-----------------
# frame resultados
#-----------------

frame_resultados= Frame(ventana_principal )
frame_resultados.config (bg="seashell3", width=20, height=100)
frame_resultados.place(x=50,y=260)

# area de texto para resultado
t_resultado=Text(frame_resultados, width=96, height=3)
t_resultado.config(bg="SkyBlue3", fg="white", font=("Arial", 20))
t_resultado.pack()
"""
ventana_principal.mainloop()