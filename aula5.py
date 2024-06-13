import customtkinter as ctk  # importando biblioteca


janela = ctk.CTk() #Criando a janela

#Configurando a janela principal
janela.title("Cadastro de Equipamentos")
janela.geometry("700x400")
janela.maxsize(width=900, height=550)
janela.minsize(width=500, height=300)
janela.resizable(width=False, height=False)

#Costumizando tema da nossa aplicação 


janela.mainloop()