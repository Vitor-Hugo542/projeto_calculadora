import tkinter as tk
from tkinter import messagebox
# Funções da Calculadora

def adicionar(valor):
    '''Adiciona um número ou operador no display'''
    display.insert(tk.END, valor)

def limpar():
    display.delete(0, tk.END)
def calcular():
    try:
        expressao = display.get()
        # Substituição de símbolos
        expressao = expressao.replace('×', '*').replace('÷', '/')
        expressao = expressao.replace('+', '+')
        resultado = eval(expressao)

        display.delete(0, tk.END)
        display.insert(tk.END, str(resultado))
    except ZeroDivisionError:
        messagebox.showerror("Erro", "Divisão por zero!")
        limpar()

# Interface
janela = tk.Tk()
janela.title("Calculator Tabajara")
janela.geometry("360x500")
janela.resizable(False, False)

# Display (Único campo)
display = tk.Entry(janela, font=("Arial", 20), justify="right", bd=13, relief="sunken")
display.grid(column=0, row=0, columnspan=4, padx=10, pady=20, ipadx=8, ipady=20)

#Lista de botões
botoes = [
    'C', '±', '%', '÷', # Linha 1
    '7', '8', '9', '×', # Linha 2
    '4', '5', '6', '-', # Linha 3
    '1', '2', '3', '+', # Linha 4
    '0', '.', '='       # Linha 5 (Ocupa 2 colunas)
]
# Cores para deixar a calculadora mais gay
cor_numero = "#ffffff" # Branco para números
cor_operador = "#ff9500" # Laranja para operados
cor_especial = "#a6a6a6" # Cinza para C, ±, %

# Criação dos botões grid
row = 1 # Começa na linha 1 (Linha 0 é o display)
col = 0 # Começa na coluna 0

for botao in botoes:
    if botao == '=':
        # Botão de igual ocupa 2 colunas e tem a cor laranja
        btn = tk.Button(janela, text= botao, font=("Arial", 18, "bold"),bg=cor_operador, fg="white", height=2, command=calcular)
        btn.grid(column=col, row=row, columnspan=2, padx=3, pady=3, sticky="nsew")
        col += 2
    elif botao == "0":
        # Botão 0 também ocupa 2 colunas
        btn = tk.Button(janela, text= botao, font=("Arial", 18, "bold"), bg=cor_especial, command=lambda v=botao: adicionar(v))
        btn.grid(column=col, row=row, columnspan=2, padx=3, pady=3, sticky="nsew")
        col += 2
    elif botao == '÷×-+':
        # Operadores matemáticos
        btn = tk.Button(janela, text=botao, font=("Arial", 18, "bold"), bg=cor_operador,fg= "white", command=lambda v=botao: adicionar(v))
        btn.grid(column=col, row=row, columnspan=2, padx=3, pady=3, sticky="nsew")
        col += 1
    elif botao in 'C±%':
        # Botões especiais
        btn = tk.Button(janela, text=botao, font=("Arial", 16), bg=cor_especial, command=limpar if botao == 'C' else lambda v=botao: calcular())
        btn.grid(column=col, row=row, columnspan=2, padx=3, pady=3, sticky="nsew")
        col += 1
    else:
        # Números normais (7,8,9,4,5,6,1,2,3)
        btn = tk.Button(janela, text=botao, font=("Arial", 18), bg=cor_especial,command=lambda v=botao: adicionar(v))
        btn.grid(column=col, row=row, columnspan=2, padx=3, pady=3, sticky="nsew")
        col += 1
# Quando chegar no final da linha(4 colunas), pula para a próxima linha
    if col > 3:
        col = 0
        row += 1

# Configuração da grid
# Faz as colunas se expandirem igualmente quando a janela for redimencionada

for i in range (4):
    janela.grid_columnconfigure(i, weight=1)

    # Faz as linhas (a partir de 1) se expandirem igualmente
for i in range(1, 6):
    janela.grid_rowconfigure(i, weight=1)

janela.mainloop()