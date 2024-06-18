import customtkinter as ctk  # importando biblioteca
 


janela = ctk.CTk()  # Criando a janela

# Configurando a janela principal
janela.title("App Teste")
janela.geometry("700x400")

ctk.CTkLabel(janela, text="Cursor de Customtkinter - Aula 06 (label)",
             font=("arial bold", 20)).pack(pady=20, padx=5)
ctk.CTkLabel(janela, text="Digite seu Nome Completo:").pack()


lab = ctk.CTkLabel(janela,
                   width=200, height=25,
                   text_color="red",
                   font=("arial bold", 16))
lab.pack(pady=10)

entry = ctk.CTkEntry(janela, width=200)

janela.mainloop()
