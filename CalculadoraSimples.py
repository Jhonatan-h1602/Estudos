import tkinter as tk


def calcular():
    try:
        expressao = entrada.get()
        resultado = str(eval(expressao))
        entrada.delete(0, tk.END)
        entrada.insert(0, resultado)
    except:
        entrada.delete(0, tk.END)
        entrada.insert(0, "Erro")


def adicionar_numero(numero):
    entrada.insert(tk.END, numero)


def adicionar_operador(operador):
    entrada.insert(tk.END, operador)


def limpar_entrada():
    entrada.delete(0, tk.END)


# Criação da janela
janela = tk.Tk()
janela.title("Calculadora")

# Campo de entrada (visor)
entrada = tk.Entry(janela, width=20, borderwidth=5)
entrada.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Botões
numeros = ['7', '8', '9', '4', '5', '6', '1', '2', '3']
operadores = ['+', '-', '*', '/']

# Cria botões dos números
linha = 1
coluna = 0
for numero in numeros:
    botao = tk.Button(janela, text=numero, padx=20, pady=20, command=lambda num=numero: adicionar_numero(num))
    botao.grid(row=linha, column=coluna)
    coluna += 1
    if coluna > 2:
        coluna = 0
        linha += 1

# Cria botões dos operadores
linha = 1
coluna = 3
for operador in operadores:
    botao = tk.Button(janela, text=operador, padx=19, pady=20, command=lambda op=operador: adicionar_operador(op))
    botao.grid(row=linha, column=coluna)
    linha += 1
    

 # Agora criamos o botão 0 manualmente
botao_zero = tk.Button(janela, text='0', padx=20, pady=20, command=lambda: adicionar_numero('0'))
botao_zero.grid(row=4, column=1)  # abaixo do número 2

# Botão de igual
botao_igual = tk.Button(janela, text="=", padx=20, pady=20, command=calcular)
botao_igual.grid(row=4, column=2)  # estava usando 'linha', mude para linha fixa

# Botão de limpar
botao_limpar = tk.Button(janela, text="C", padx=20, pady=20, command=limpar_entrada)
botao_limpar.grid(row=4, column=0)  # sobe para a mesma linha do '='


# Executa a janela
janela.mainloop()
