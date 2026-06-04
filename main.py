import tkinter as tk
import json


# ==========================
# FUNÇÕES
# ==========================

def adicionar_tarefa():

    tarefa = entrada.get()

    if tarefa:
        lista.insert(tk.END, tarefa)
        entrada.delete(0, tk.END)


def remover_tarefa():

    try:
        indice = lista.curselection()[0]
        lista.delete(indice)

    except:
        pass


def concluir_tarefa():

    try:

        indice = lista.curselection()[0]

        tarefa = lista.get(indice)

        if not tarefa.startswith("✓ "):

            lista.delete(indice)

            lista.insert(
                indice,
                f"✓ {tarefa}"
            )

    except:
        pass


def salvar_tarefas():

    with open("tarefas.txt", "w", encoding="utf-8") as arquivo:

        for tarefa in lista.get(0, tk.END):
            arquivo.write(tarefa + "\n")


def carregar_tarefas():

    try:

        with open("tarefas.txt", "r", encoding="utf-8") as arquivo:

            for linha in arquivo:
                lista.insert(
                    tk.END,
                    linha.strip()
                )

    except FileNotFoundError:
        pass


# ==========================
# JANELA
# ==========================

janela = tk.Tk()

janela.title("Gerenciador de Tarefas")

janela.geometry("500x600")

janela.configure(bg="#f5f5f5")


# ==========================
# TÍTULO
# ==========================

titulo = tk.Label(
    janela,
    text="Gerenciador de Tarefas",
    font=("Arial", 20, "bold"),
    bg="#f5f5f5"
)

titulo.pack(pady=20)


# ==========================
# CAMPO DE TEXTO
# ==========================

entrada = tk.Entry(
    janela,
    width=40,
    font=("Arial", 12)
)

entrada.pack(pady=10)


# ==========================
# BOTÕES
# ==========================

btn_adicionar = tk.Button(
    janela,
    text="Adicionar",
    command=adicionar_tarefa,
    width=20
)

btn_adicionar.pack(pady=5)


btn_concluir = tk.Button(
    janela,
    text="Concluir",
    command=concluir_tarefa,
    width=20
)

btn_concluir.pack(pady=5)


btn_remover = tk.Button(
    janela,
    text="Remover",
    command=remover_tarefa,
    width=20
)

btn_remover.pack(pady=5)


btn_salvar = tk.Button(
    janela,
    text="Salvar",
    command=salvar_tarefas,
    width=20
)

btn_salvar.pack(pady=5)


# ==========================
# LISTA
# ==========================

lista = tk.Listbox(
    janela,
    width=50,
    height=15,
    font=("Arial", 12)
)

lista.pack(pady=20)


# ==========================
# CARREGAR DADOS
# ==========================

carregar_tarefas()


# ==========================
# EXECUTAR
# ==========================

janela.mainloop()