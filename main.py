import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Função para adicionar a tarefa
def adicionar_tarefa():
    nome = entrada_nome.get()
    data = entrada_data.get()
    hora = entrada_hora.get()
    descricao = entrada_descricao.get()

    # Verifica se os campos não estão vazios
    if nome and data and hora and descricao:
        # Insere a tarefa na tabela
        tabela.insert("", "end", values=(nome, data, hora, descricao, "X"))
        # Limpa os campos de entrada
        entrada_nome.delete(0, "end")
        entrada_data.delete(0, "end")
        entrada_hora.delete(0, "end")
        entrada_descricao.delete(0, "end")
        # Adiciona um botão "X" para excluir o registro
        idx = tabela.index("end")  # Obtém o índice do último registro
    else:
        messagebox.showwarning("Erro", "Por favor, preencha todos os campos.")

# Função para excluir uma tarefa
def excluir_tarefa(event):
    coluna_clicada = tabela.identify_column(event.x)  # Identifica a coluna clicada
    print("Coluna clicada é " + coluna_clicada)
    if coluna_clicada == "#5":  # Verifica se a coluna é a de exclusão
        item = tabela.identify_row(event.y)  # Obtém o item (linha) selecionado
        tabela.delete(item)  # Remove o item selecionado da tabela

# Função para formatar data no formato dd/mm/yyyy enquanto o usuário digita
def formatar_data(event):
    data = entrada_data.get()
    if len(data) == 2:
        entrada_data.insert(tk.END, '/')
    if len(data) == 5:
        entrada_data.insert(tk.END, '/')

# Função para formatar hora no formato hh:mm enquanto o usuário digita
def formatar_hora(event):
    hora = entrada_hora.get()
    if len(hora) == 2:
        entrada_hora.insert(tk.END, ':')

# Cria a janela principal
root = tk.Tk()
root.title("Gerenciamento de Tarefas")

# Define as dimensões da janela e impede a maximização e redimensionamento
root.resizable(False, False)  # Impede o redimensionamento da janela

# Frame para campos de entrada
frame_campos = tk.Frame(root, padx=10, pady=10)
frame_campos.pack()

# Campos de entrada
tk.Label(frame_campos, text="Nome da Tarefa:").grid(row=0, column=0)
entrada_nome = tk.Entry(frame_campos)
entrada_nome.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame_campos, text="Data da Tarefa (dd/mm/yyyy):").grid(row=1, column=0)
entrada_data = tk.Entry(frame_campos)
entrada_data.grid(row=1, column=1, padx=5, pady=5)
entrada_data.bind('<KeyRelease>', formatar_data)

tk.Label(frame_campos, text="Horário da Tarefa (hh:mm):").grid(row=2, column=0)
entrada_hora = tk.Entry(frame_campos)
entrada_hora.grid(row=2, column=1, padx=5, pady=5)
entrada_hora.bind('<KeyRelease>', formatar_hora)

tk.Label(frame_campos, text="Descrição:").grid(row=3, column=0)
entrada_descricao = tk.Entry(frame_campos)
entrada_descricao.grid(row=3, column=1, padx=5, pady=5)

# Botão para adicionar a tarefa
botao_inserir = tk.Button(frame_campos, text="Inserir Tarefa", command=adicionar_tarefa)
botao_inserir.grid(row=4, columnspan=2, padx=5, pady=5)

# Frame para a tabela de tarefas
frame_tabela = tk.Frame(root, padx=10, pady=10)
frame_tabela.pack()

# Cria a tabela
colunas = ("Nome da Tarefa", "Data", "Horário", "Descrição", "#")
tabela = ttk.Treeview(frame_tabela, columns=colunas, show="headings")

# Define os títulos das colunas
for col in colunas:
    tabela.heading(col, text=col)
    tabela.column(col, anchor="center")

tabela.column("Data", width=90, anchor="center")
tabela.column("Horário", width=90, anchor="center")
tabela.column("Descrição", width=400, anchor="center")
tabela.column("#", width=50, anchor="center")  # Definindo a largura da coluna com os botões "X"

tabela.pack()

# Vincula a função para excluir à tabela
tabela.bind('<Button-1>', excluir_tarefa)

root.mainloop()
