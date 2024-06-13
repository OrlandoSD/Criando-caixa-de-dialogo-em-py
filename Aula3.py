import customtkinter as ctk  # importando biblioteca

# Criando a janela
janela = ctk.CTk()

# Configurando a janela principal
janela.title("Cadastro de Equipamentos")
janela.geometry("700x400")
janela.maxsize(width=900, height=550)
janela.minsize(width=500, height=300)
janela.resizable(width=False, height=False)

# Aula 3  = tabWiew (Abas no tkinter)
tabview = ctk.CTkTabview(janela, width=400)
tabview.pack()
tabview.add("Nomes")
tabview.add("Genero")
tabview.add("Idades")
tabview.tab("Nomes").grid_columnconfigure(0, weight=1)
tabview.tab("Genero").grid_columnconfigure(0, weight=1)
tabview.tab("Idades").grid_columnconfigure(0, weight=1)

# Adicionando elementos nas abas
label_nomes = ctk.CTkLabel(tabview.tab("Nomes"), text="Eduardo Bandeira\nEufrazio Graber\nGeraldo Costa\nAntonio Marcos")
label_nomes.pack()

label_idades = ctk.CTkLabel(tabview.tab("Idades"), text="45\n18\n49\n76")
label_idades.pack()

janela.mainloop()
