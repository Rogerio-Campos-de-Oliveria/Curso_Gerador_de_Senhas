from tkinter import *
from tkinter import ttk

# Importanto Pillow
from PIL import ImageTk, Image

# Cores ---------------------------

color0 = '#444466'  # Preta / Black
color1 = '#feffff'  # Branca / White
color2 = '#f05a43'  # Vermelha / Red

janela = Tk()
janela.title('')
janela.geometry('295x350')
janela.configure(bg=color1)

# dividindo a tela em dois fremes ----------------------------------------------------
frame_cima = Frame(janela, width=295, height=50, bg=color1, pady=0, padx=0, relief='flat')
frame_cima.grid(row=0, column=0, sticky=NSEW)

frame_baixo = Frame(janela, width=295, height=310, bg=color0, pady=0, padx=0, relief='flat')
frame_baixo.grid(row=1, column=0, sticky=NSEW)

# Trabalhando no frame Cima ------------------
img = Image.open('logo.png')
img = img.resize((30, 30), Image.LANCZOS)
img = ImageTk.PhotoImage(img)

app_logo = Label(frame_cima, height=60, image=img, compound=LEFT, padx=10, relief='flat', anchor='nw', bg=color1)
app_logo.place(x=2, y=0)

estilo = ttk.Style(janela)
estilo.theme_use('clam')

janela.mainloop()
