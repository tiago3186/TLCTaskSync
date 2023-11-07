import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Função para adicionar a tarefa
def adicionar_tarefa():
    nome = entrada_nome.get()
    data = entrada_data.get()

    # Verifica se os campos não estão vazios
    if nome and data:
        # Insere a tarefa na tabela
        tabela.insert("", "end", values=(nome, data))
        # Limpa os campos de entrada
        entrada_nome.delete(0, "end")
        entrada_data.delete(0, "end")
    else:
        messagebox.showwarning("Erro", "Por favor, preencha todos os campos.")

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

# Botão para adicionar a tarefa
botao_inserir = tk.Button(frame_campos, text="Inserir Tarefa", command=adicionar_tarefa)
botao_inserir.grid(row=2, columnspan=2)

# Frame para a tabela de tarefas
frame_tabela = tk.Frame(root)
frame_tabela.pack()

# Cria a tabela
colunas = ("Nome da Tarefa", "Data da Tarefa")
tabela = ttk.Treeview(frame_tabela, columns=colunas, show="headings")

# Define os títulos das colunas
for col in colunas:
    tabela.heading(col, text=col)
    tabela.column(col, anchor="center")
tabela.pack()

root.mainloop()
