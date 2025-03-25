from tkinter import *
from db import *

#### Definindo algumas cores p/ utilizar no projeto ######

co0 = "#000000"  # preta
co1 = "#59656F"
co2 = "#feffff"  # branca
co3 = "#0074eb"  # azul
co4 = "#f04141"  # vermelho
co5 = "#59b356"  # verde
co6 = "cdd1cd"   # cizenta

#### Criando a janela principal ####

root = Tk()
root.resizable(width=FALSE, height=FALSE)
root.geometry('500x225')  # largura e altura da janela  
root.title('To-do App')
root.configure(background=co1)


### Dividindo a janela em duas partes ####

frame_esquerda=Frame(root, width=300, height=200, bg=co2, relief="flat")
frame_esquerda.grid(row=0, column=0, sticky=NSEW)    # NSEW == North, South, West e East. Com isso irá preencher tudo.

frame_direita=Frame(root, width=200, height=250, bg=co2, relief="flat")
frame_direita.grid(row=0, column=1, sticky=NSEW)    # NSEW == North, South, West e East. Com isso irá preencher tudo.

#### Divindindo o frame a esquerda em duas partes ####

frame_e_cima=Frame(frame_esquerda, width=300, height=50, bg=co2, relief="flat")  # Frame esquerda em cima
frame_e_cima.grid(row=0, column=0, sticky=NSEW)

frame_e_baixo=Frame(frame_esquerda, width=300, height=150, bg=co2, relief="flat")  
frame_e_baixo.grid(row=1, column=0, sticky=NSEW)


def main(a):
    #### novo ####
    if a == "novo":
        for widget in frame_e_baixo.winfo_children():
            widget.destroy()
       
        
        def adicionar():
            tarefa_entry=entry.get()
            inserir([tarefa_entry])   
            mostrar()  


        lb=Label(frame_e_baixo, text="Insira nova tarefa", font=("Arial 9 bold"), width=40,height=5, pady=15,  
                relief="flat", anchor=CENTER, bg=co2, fg=co0)
        lb.grid(row=0, column=0, sticky=NSEW, pady=1)

        entry = Entry(frame_e_baixo, width=15, bg="black", fg="white", justify='center')
        entry.grid(row=1, column=0, sticky=NSEW)

        btn_adicionar=Button(frame_e_baixo,text="Adicionar", width=9, height=1, 
                    bg=co0, fg=co2, font="7", anchor="center", relief="raised", command=adicionar)
        btn_adicionar.grid(row=2, column=0, pady=16)

    #### atualizar ####
    if a == "atualizar":
        for widget in frame_e_baixo.winfo_children():
            widget.destroy()

        def on():
            

            lb=Label(frame_e_baixo, text="Atualizar as tarefas", font=("Arial 9 bold"), width=40,height=5, pady=15,  
                    relief="flat", anchor=CENTER, bg=co2, fg=co0)
            lb.grid(row=0, column=0, sticky=NSEW, pady=1)

            entry = Entry(frame_e_baixo, width=15, bg="black", fg="white", justify='center')
            entry.grid(row=1, column=0, sticky=NSEW)
            
            v_selecionado=listbox.curselection()[0]
            palavra=listbox.get(v_selecionado)
            entry.insert(0,palavra)

            tarefas = selecionar()

            def alterar():
                for item in tarefas: 
                    if palavra == item[1]:
                        nova=[entry.get(), item[0]]
                        atualizar(nova)
                        entry.delete(0,END)

                mostrar()
            btn_alterar=Button(frame_e_baixo,text="Atualizar", width=9, height=1, 
                        bg=co0, fg=co2, font="7", anchor="center", relief="raised", command=alterar)
            btn_alterar.grid(row=2, column=0, pady=16)
        on()


#### Função remover ####

def remover():
    v_selecionado=listbox.curselection()[0]
    palavra=listbox.get(v_selecionado)
    tarefas = selecionar()

    for item in tarefas: 
        if palavra == item[1]:
            deletar([item[0]])
        
    mostrar()

#### Criando botões "novo", "remover" e "atualizar" ####

btn_novo=Button(frame_e_cima,text="Novo", width=10, height=1, 
                bg=co3, fg="white", font="5", anchor="center", relief="raised", command=lambda:main("novo"))
btn_novo.grid(row=0, column=0, sticky=NSEW, pady=1)

btn_remover=Button(frame_e_cima,text="Remover", width=10, height=1, 
                bg=co4, fg="white", font="5", anchor="center", relief="raised",command=remover)
btn_remover.grid(row=0, column=1, sticky=NSEW, pady=1)

btn_atualizar=Button(frame_e_cima,text="Atualizar", width=10, height=1, 
                bg=co5, fg="white", font="5", anchor="center", relief="raised", command=lambda:main("atualizar"))
btn_atualizar.grid(row=0, column=2, sticky=NSEW, pady=1)

#### Adicionando listbox e um label ####

label=Label(frame_direita, text="Tarefas", width=37,height=1, pady=7, padx=15, 
            relief="flat", anchor=W, font=("Arial 20 bold"), bg=co2, fg=co0)
label.grid(row=0, column=0, sticky=NSEW, pady=1)

listbox = Listbox(frame_direita, font=("Arial 9 bold"), width=1)
listbox.grid(row=1, column=0, sticky=NSEW, pady=5)

### Adicionando tarefas na listbox ####

def mostrar():
    listbox.delete(0,END)     # Isso impede de mostrar duplicadamente os itens ao adicionar um novo
    tarefas= selecionar()
    for item in tarefas:
        listbox.insert(END, item[1])

mostrar()
#### Front-End completo ^



root.mainloop()
