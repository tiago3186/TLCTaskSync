import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Função para adicionar a tarefa
def adicionar_tarefa():
    nome = entrada_nome.get()
    data = entrada_data.get()
    hora = entrada_hora.get()

    # Verifica se os campos não estão vazios
    if nome and data and hora:
        # Insere a tarefa na tabela
        tabela.insert("", "end", values=(nome, data, hora, "X"))
        # Limpa os campos de entrada
        entrada_nome.delete(0, "end")
        entrada_data.delete(0, "end")
        entrada_hora.delete(0, "end")
        # Adiciona um botão "X" para excluir o registro
        idx = tabela.index("end")  # Obtém o índice do último registro
        
    else:
        messagebox.showwarning("Erro", "Por favor, preencha todos os campos.")

# Função para excluir uma tarefa
def excluir_tarefa(event):
    item = tabela.selection()[0]  # Obtém o item selecionado
    tabela.delete(item)  # Remove o item selecionado da tabela

# Cria a janela principal
root = tk.Tk()
root.title("Gerenciamento de Tarefas")

# Frame para campos de entrada
frame_campos = tk.Frame(root)
frame_campos.pack()

# Campos de entrada
tk.Label(frame_campos, text="Nome da Tarefa:").grid(row=0, column=0)
entrada_nome = tk.Entry(frame_campos)
entrada_nome.grid(row=0, column=1)

tk.Label(frame_campos, text="Data da Tarefa:").grid(row=1, column=0)
entrada_data = tk.Entry(frame_campos)
entrada_data.grid(row=1, column=1)

tk.Label(frame_campos, text="Horário da Tarefa:").grid(row=2, column=0)
entrada_hora = tk.Entry(frame_campos)
entrada_hora.grid(row=2, column=1)

# Botão para adicionar a tarefa
botao_inserir = tk.Button(frame_campos, text="Inserir Tarefa", command=adicionar_tarefa)
botao_inserir.grid(row=3, columnspan=2)

# Frame para a tabela de tarefas
frame_tabela = tk.Frame(root)
frame_tabela.pack()

# Cria a tabela
colunas = ("Nome da Tarefa", "Data da Tarefa", "Horário da Tarefa", "#")
tabela = ttk.Treeview(frame_tabela, columns=colunas, show="headings")

# Define os títulos das colunas
for col in colunas:
    tabela.heading(col, text=col)
    tabela.column(col, anchor="center")

tabela.column("#", width=50, anchor="center")  # Definindo a largura da coluna com os botões "X"

tabela.pack()

# Vincula a função para excluir à tabela
tabela.bind('<Button-1>', excluir_tarefa)

root.mainloop()

