import customtkinter as ctk  # importando biblioteca


janela = ctk.CTk() #Criando a janela

#Configurando a janela principal
janela.title("Cadastro de Equipamentos")
janela.geometry("700x400")
janela.maxsize(width=900, height=550)
janela.minsize(width=500, height=300)
janela.resizable(width=False, height=False)

#Aula 2  = Frames

frame1 = ctk.CTkFrame(master = janela, width=200, height=330,fg_color="teal", bg_color="transparent", border_width=10, corner_radius=30).place(x=20, y=60)
frame2 = ctk.CTkFrame(master = janela, width=200, height=330, fg_color="green").place(x=240, y=60)
frame3 = ctk.CTkFrame(master = janela, width=200, height=330, fg_color="white").place(x=460, y=60)

janela.mainloop()