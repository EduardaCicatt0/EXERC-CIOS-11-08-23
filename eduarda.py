import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def trabalho():
    nome = Ins_nome.get()
    mensagem = Ins_mensagem.get()
    
    if nome and mensagem:
        Mens_Janela = tk.Toplevel(janela)
        Mens_Janela.title('Mensagem Enviada')
        Labelmensagem = tk.Label(Mens_Janela, text=f"{nome} diz {mensagem}")
        Labelmensagem.pack()
        janela.wait_window(Mens_Janela)
    else:
        messagebox.showerror("Erro", "Por favor, insira o nome e a mensagem")

janela = tk.Tk()
janela.title("Prova diagnóstica")
janela.geometry("250x250")

Nome = tk.Label(janela, text="Nome")
Nome.pack()
Ins_nome = tk.Entry(janela)
Ins_nome.pack()

mensagem = tk.Label(janela, text="Mensagem")
mensagem.pack()
Ins_mensagem = tk.Entry(janela)
Ins_mensagem.pack()

botao = tk.Button(janela, text="Enviar", command=trabalho)
botao.pack()

Men_espera = tk.Label(janela, text="Aguardando mensagem do usuário")
Men_espera.pack()

janela.mainloop()