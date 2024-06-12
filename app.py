import customtkinter as ctk  # importando biblioteca


janela = ctk.CTk() #Criando a janela

#Configurando a janela principal
janela.title("Cadastro de Equipamentos")
janela.geometry("700x400")
janela.maxsize(width=900, height=550)
janela.minsize(width=500, height=300)
janela.resizable(width=False, height=False)

#Costumizando tema da nossa aplicação 
#janela._set_appearance_mode("System")
janela._set_appearance_mode("dark")

#Criando nova janela
def nova_tela():
    nova_janela = ctk.CTkToplevel(janela)
    nova_janela.geometry("300x200")

btn_nova_tela = ctk.CTkButton(master=janela, text="Abrir nova Janela", command=nova_tela).place(x=300, y=100)

janela.mainloop()