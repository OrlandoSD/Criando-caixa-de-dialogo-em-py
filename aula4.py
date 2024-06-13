import customtkinter as ctk  # importando biblioteca

# Criando a janela
janela = ctk.CTk()

# Configurando a janela principal
janela.title("Cadastro de Equipamentos")
janela.geometry("700x400")
janela.maxsize(width=900, height=550)
janela.minsize(width=500, height=300)
janela.resizable(width=False, height=False)

# Aula 3  = tabView (Abas no tkinter)
tabview = ctk.CTkTabview(janela, width=400, corner_radius=20, border_width=1, border_color="red",fg_color="teal", segmented_button_selected_color="green", segmented_button_unselected_hover_color="blue", segmented_button_unselected_color="black")
tabview.pack()
tabview.add("Nomes")
tabview.add("Genero")
tabview.add("Idades")
tabview.tab("Nomes").grid_columnconfigure(0, weight=1)
tabview.tab("Genero").grid_columnconfigure(0, weight=1)
tabview.tab("Idades").grid_columnconfigure(0, weight=1)

# Dados a serem exibidos
nomes = ["Eduardo Bandeira", "Eufrazio Graber", "Geraldo Costa", "Antonio Marcos"]
idades = ["45", "18", "49", "76"]
genero = ["masculino", "Masculino", "Masculino", "Feminino"]

# Função para criar uma tabela
def criar_tabela(tab, headers, data):
    for col, header in enumerate(headers):
        lbl_header = ctk.CTkLabel(tab, text=header, font=('Arial', 12, 'bold'))
        lbl_header.grid(row=0, column=col, padx=5, pady=5)
    
    for row, item in enumerate(data, start=1):
        for col, value in enumerate(item):
            lbl_value = ctk.CTkLabel(tab, text=value, font=('Arial', 12))
            lbl_value.grid(row=row, column=col, padx=5, pady=5)

# Criando tabelas nas abas
# Aba Nomes
headers_nomes = ["Nome"]
dados_nomes = [[nome] for nome in nomes]
criar_tabela(tabview.tab("Nomes"), headers_nomes, dados_nomes)

# Aba Idades
headers_idades = ["Idade"]
dados_idades = [[idade] for idade in idades]
criar_tabela(tabview.tab("Idades"), headers_idades, dados_idades)

#Aba Genero
headers_genero = ["Genero"]
dados_genero = [[genero] for genero in genero]
criar_tabela(tabview.tab("Genero"), headers_genero, dados_genero)

janela.mainloop()
