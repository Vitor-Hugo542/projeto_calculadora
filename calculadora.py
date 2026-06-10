import tkinter as tk
from tkinter import messagebox
# Funções da Calculadora

def adicionar(valor):
    '''Adiciona u m número ou operador no display'''
    display.insert(tk.END, valor)

def limpar():
    try:
        expressao = display.get()
        # Substituição de símbolos
        expressao = expressao.replace('x', '*').replace('÷', '/')
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
display = tk.Entry(janela, font=("Arial", 24), justify="right", bd=13, relief="sunken")
display.grid(column=0, row=0, columnspan=4, padx=10, pady=20, ipadx=8, ipady=20)

#Lista de botões
botoes = [
    'C', '±', '%', '÷', # Linha 1
    '7', '8', '9', 'X', # Linha 2
    '4', '5', '6', '-', # Linha 3
    '1', '2', '3', '+', # Linha 4
    '0', '.', '='       # Linha 5 (Ocupa 2 colunas)
]
# Cores para deixar a calculadora mais gay
cor_numero = "#ffffff" # Branco para números
cor_numero = "#ff9500" # Laranja para operados
cor_especial = "#a6a6a6" # Cinza para C, ±, %

janela.mainloop()