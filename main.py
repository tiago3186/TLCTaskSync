import tkinter as tk
from tkinter import ttk, filedialog
from tkinter import messagebox
import os

fileName = ""  # Variável para armazenar o nome do arquivo da agenda
fileDir = ""  # Variável para armazenar o diretório do arquivo da agenda

# Funções para as opções do menu
def nova_agenda():
    resposta = messagebox.askquestion("Gerar Nova Agenda", "Deseja gerar uma nova agenda em branco?")
    if resposta == 'yes':
        for item in tabela.get_children():
            tabela.delete(item)

def salvar_agenda():
    global fileName  # Utilize a variável global fileName
    global fileDir

    if not fileName:  # Se fileName estiver vazio
        filepath = filedialog.asksaveasfilename(defaultextension=".agn", filetypes=(("Agenda Files", "*.agn"), ("All Files", "*.*")))
        if filepath:
            fileName = os.path.basename(filepath)  # Atualiza o fileName com o nome do arquivo
            fileDir = os.path.dirname(filepath)
            print(fileDir)
            with open(filepath, 'w') as file:
                for item in tabela.get_children():
                    values = tabela.item(item)['values']
                    file.write(','.join(values) + '\n')
    else:
        # Se fileName não estiver vazio, salva por cima do arquivo existente
        filepath = os.path.join(fileDir, fileName)
        with open(filepath, 'w') as file:
            for item in tabela.get_children():
                values = tabela.item(item)['values']
                file.write(','.join(values) + '\n')
                print(filepath)
               

def salvar_agenda_como():
    global fileName  # Utilize a variável global fileName

    filepath = filedialog.asksaveasfilename(defaultextension=".agn", filetypes=(("Agenda Files", "*.agn"), ("All Files", "*.*")))
    if filepath:
        fileName = os.path.basename(filepath)  # Atualiza o fileName com o nome do arquivo
        with open(filepath, 'w') as file:
            for item in tabela.get_children():
                values = tabela.item(item)['values']
                file.write(','.join(values) + '\n')

def carregar_agenda():
    filepath = filedialog.askopenfilename(filetypes=(("Agenda Files", "*.agn"), ("All Files", "*.*")))
    if filepath:
        # Limpar a tabela
        for item in tabela.get_children():
            tabela.delete(item)

        # Carregar dados do arquivo selecionado para a tabela
        with open(filepath, 'r') as file:
            for line in file:
                values = line.strip().split(',')
                tabela.insert("", "end", values=values)

def sair():
    root.destroy()

def ajuda():
    # Lógica para fornecer ajuda
    pass

def sobre():
    janela_sobre = tk.Toplevel(root)
    janela_sobre.title("Sobre")
    
    # Carregar a imagem
    imagem = tk.PhotoImage(file="agenda.png")
    
    # Exibir a imagem à esquerda
    label_imagem = tk.Label(janela_sobre, image=imagem)
    label_imagem.image = imagem  # Mantém uma referência à imagem
    
    label_imagem.grid(row=0, column=0, padx=10, pady=10, rowspan=3)
    
    # Textos
    label_nome_app = tk.Label(janela_sobre, text="TLC TaskSync 2023", font=("Arial", 14, "bold"))
    label_nome_app.grid(row=0, column=1, padx=10, pady=10)
    
    label_desenvolvedor = tk.Label(janela_sobre, text="Desenvolvido por Tiago Custódio", font=("Arial", 12))
    label_desenvolvedor.grid(row=1, column=1, padx=10, pady=5)
    
    # Função para fechar a janela "Sobre"
    def fechar_janela():
        janela_sobre.destroy()
    
    # Botão OK para fechar a janela
    botao_ok = tk.Button(janela_sobre, text="OK", command=fechar_janela)
    botao_ok.grid(row=2, column=1, padx=10, pady=10)

# Função para adicionar a tarefa
def adicionar_tarefa():
    nome = entrada_nome.get()
    data = entrada_data.get()
    hora = entrada_hora.get()
    descricao = entrada_descricao.get()

    if nome and data and hora and descricao:
        if validar_data(data) and validar_hora(hora):
            tabela.insert("", "end", values=(nome, data, hora, descricao, "X"))
            entrada_nome.delete(0, "end")
            entrada_data.delete(0, "end")
            entrada_hora.delete(0, "end")
            entrada_descricao.delete(0, "end")
        else:
            messagebox.showwarning("Erro", "Formato de data ou hora inválido.")
    else:
        messagebox.showwarning("Erro", "Por favor, preencha todos os campos.")

# Função para ordenar as tarefas por data e horário
def ordenar_tarefas():
    tarefas = [(tabela.item(item)['values'][1], tabela.item(item)['values'][2], item) for item in tabela.get_children()]
    tarefas_ordenadas = sorted(tarefas, key=lambda x: (x[0], x[1]))  # Ordena primeiro por data e secundariamente por horário

    # Reinsere as tarefas na tabela na ordem classificada
    for index, (data, hora, item) in enumerate(tarefas_ordenadas):
        tabela.move(item, '', index)

# Função para verificar se a data está no formato correto
def validar_data(data):
    # Verifica se a data tem o formato dd/mm/yyyy e se o dia e mês estão dentro dos limites
    try:
        dia, mes, ano = map(int, data.split('/'))
        return 1 <= dia <= 31 and 1 <= mes <= 12
    except ValueError:
        return False

# Função para verificar se a hora está no formato correto
def validar_hora(hora):
    # Verifica se a hora tem o formato hh:mm e se a hora e minutos estão dentro dos limites
    try:
        horas, minutos = map(int, hora.split(':'))
        return 0 <= horas <= 23 and 0 <= minutos <= 59
    except ValueError:
        return False

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
    if len(data) == 2 or len(data) == 5:
        entrada_data.insert(tk.END, '/')
    elif len(data) >= 10:
        entrada_data.delete(10, tk.END)  # Limite de 10 caracteres, exclui qualquer entrada adicional

# Função para formatar hora no formato hh:mm enquanto o usuário digita
def formatar_hora(event):
    hora = entrada_hora.get()
    if len(hora) == 2:
        entrada_hora.insert(tk.END, ':')
    elif len(hora) >= 5:
        entrada_hora.delete(5, tk.END)  # Limite de 5 caracteres, exclui qualquer entrada adicional


# Cria a janela principal
root = tk.Tk()
root.title("TLC TaskSync 2023")
root.iconbitmap('agenda.ico')

# Define as dimensões da janela e impede a maximização e redimensionamento
root.resizable(False, False)  # Impede o redimensionamento da janela

# Cria a barra de menus
barra_menu = tk.Menu(root)

# Menu Arquivo
menu_arquivo = tk.Menu(barra_menu, tearoff=0)
menu_arquivo.add_command(label="Novo", command=nova_agenda)
menu_arquivo.add_command(label="Salvar", command=salvar_agenda)
menu_arquivo.add_command(label="Salvar Como", command=salvar_agenda_como)
menu_arquivo.add_command(label="Carregar", command=carregar_agenda)
menu_arquivo.add_separator()
menu_arquivo.add_command(label="Sair", command=sair)
barra_menu.add_cascade(label="Arquivo", menu=menu_arquivo)

# Menu Editar
menu_editar = tk.Menu(barra_menu, tearoff=0)
# Aqui você pode adicionar opções para o menu Editar, se necessário
barra_menu.add_cascade(label="Editar", menu=menu_editar)

# Menu Ferramentas
menu_ferramentas = tk.Menu(barra_menu, tearoff=0)
# Aqui você pode adicionar opções para o menu Ferramentas, se necessário
barra_menu.add_cascade(label="Ferramentas", menu=menu_ferramentas)

# Menu Ajuda
menu_ajuda = tk.Menu(barra_menu, tearoff=0)
menu_ajuda.add_command(label="Ajuda", command=ajuda)
menu_ajuda.add_command(label="Sobre", command=sobre)
barra_menu.add_cascade(label="Ajuda", menu=menu_ajuda)

root.config(menu=barra_menu)

# Frame para campos de entrada
frame_campos = tk.Frame(root, padx=10, pady=10)
frame_campos.pack()

# Campos de entrada
tk.Label(frame_campos, text="Nome da Tarefa:").grid(row=0, column=0, sticky='w')
entrada_nome = tk.Entry(frame_campos)
entrada_nome.grid(row=0, column=1, padx=5, pady=5, sticky='w')

tk.Label(frame_campos, text="Data da Tarefa (dd/mm/yyyy):").grid(row=1, column=0, sticky='w')
entrada_data = tk.Entry(frame_campos)
entrada_data.grid(row=1, column=1, padx=5, pady=5, sticky='w')
entrada_data.bind('<KeyRelease>', formatar_data)

tk.Label(frame_campos, text="Horário da Tarefa (hh:mm):").grid(row=2, column=0, sticky='w')
entrada_hora = tk.Entry(frame_campos)
entrada_hora.grid(row=2, column=1, padx=5, pady=5, sticky='w')
entrada_hora.bind('<KeyRelease>', formatar_hora)

tk.Label(frame_campos, text="Descrição:").grid(row=3, column=0, sticky='w')
entrada_descricao = tk.Entry(frame_campos, width=45)
entrada_descricao.grid(row=3, column=1, padx=5, pady=5, sticky='w')

# Botão para adicionar a tarefa
botao_inserir = tk.Button(frame_campos, text="Inserir Tarefa", command=adicionar_tarefa)
botao_inserir.grid(row=4, column=1, padx=5, pady=5, sticky='w')

# Botão para ordenar as tarefas
botao_ordenar = tk.Button(frame_campos, text="Ordenar Tarefas", command=ordenar_tarefas)
botao_ordenar.grid(row=4, column=1, padx=5, pady=5)


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