from tkinter import *
#Criando Janela e Frames
root = Tk()
root.title('Cadastro')
fr1 = LabelFrame(root, padx=10, pady=10, bg='#49A', text='Dados Pessoais', font='Arial 25')
fr2 = LabelFrame(root, padx=10, pady=10, bg='#49A', text='Endereço', font='Arial 25')
fr3 = LabelFrame(root, padx=10, pady=10, bg='#49A', font='Arial 25')
root.configure(bg='#49A')
#Configuração da Janela:
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(2, weight=1)
root.grid_columnconfigure(0, weight=1)
#Label do 1º Frame:
lb1_fr1 = Label(fr1, text='Nome:', font='Arial 25', padx=15, pady=10, bg='#49A')
lb2_fr1 = Label(fr1, text='Data Nasc.:', font='Arial 25', padx=15, pady=10, bg='#49A')
lb3_fr1 = Label(fr1, text='CPF:', font='Arial 25', padx=15, pady=10, bg='#49A')
lb4_fr1 = Label(fr1, text='Telefone:', font='Arial 25', padx=15, pady=10, bg='#49A')
#Entry do 1º Frame:
in1_fr1 = Entry(fr1, font='Arial 25')
in2_fr1 = Entry(fr1, font='Arial 25')
in3_fr1 = Entry(fr1, font='Arial 25')
in4_fr1 = Entry(fr1, font='Arial 25')
#Posição dos Label do 1º Frame:
lb1_fr1.grid(row=1, column=0, sticky=W)
lb2_fr1.grid(row=2, column=0, sticky=W)
lb3_fr1.grid(row=3, column=0, sticky=W)
lb4_fr1.grid(row=4, column=0, sticky=W)
#Posição dos Entry do 1º Frame:
in1_fr1.grid(row=1, column=1, sticky=W)
in2_fr1.grid(row=2, column=1, sticky=W)
in3_fr1.grid(row=3, column=1, sticky=W)
in4_fr1.grid(row=4, column=1, sticky=W)
#Label do 2º Frame:
lb1_fr2 = Label(fr2, text='Rua:', font='Arial 25', padx=15, pady=10, bg='#49A')
lb2_fr2 = Label(fr2, text='Bairro:', font='Arial 25', padx=15, pady=10, bg='#49A')
lb3_fr2 = Label(fr2, text='Cidade:', font='Arial 25', padx=15, pady=10, bg='#49A')
lb4_fr2 = Label(fr2, text='Nº:', font='Arial 25', padx=15, pady=10, bg='#49A')
lb5_fr2 = Label(fr2, text='UF:', font='Arial 25', padx=15, pady=10, bg='#49A')
#Entry do 2º Frame:
in1_fr2 = Entry(fr2, font='Arial 25')
in2_fr2 = Entry(fr2, font='Arial 25')
in3_fr2 = Entry(fr2, font='Arial 25')
in4_fr2 = Entry(fr2, font='Arial 25')
in5_fr2 = Entry(fr2, font='Arial 25')
#Pack
fr1.grid(sticky=W)
fr2.grid(sticky=W)
fr3.grid(sticky=W)
#Posição dos Label do 2º Frame:
lb1_fr2.grid(row=1, column=0, sticky=W)
lb2_fr2.grid(row=2, column=0, sticky=W)
lb3_fr2.grid(row=2, column=2, sticky=W)
lb4_fr2.grid(row=1, column=4, sticky=W)
lb5_fr2.grid(row=2, column=4, sticky=W)
#Posição dos Entry do 2º Frame:
in1_fr2.grid(row=1, column=1, columnspan= 3, sticky=NSEW)
in2_fr2.grid(row=2, column=1, sticky=W)
in3_fr2.grid(row=2, column=3, sticky=W)
in4_fr2.grid(row=1, column=5, sticky=W)
in5_fr2.grid(row=2, column=5, sticky=W)
#Criando dois buttons no 3º Frame:
bt0_fr3 = Button(fr3, text='Gravar Dados', font='Arial 25',bg='green')
bt1_fr3 = Button(fr3, text='Listar Dados', font='Arial 25',bg='green')
#Posição os buttons no 3º Frame:
bt0_fr3.grid(row=0, column=0, sticky=W)
bt1_fr3.grid(row=0, column=1, sticky=W)
#Configuração da Janela do 1º Frame:
lb1_fr1.grid_rowconfigure(1, weight=1)
lb1_fr1.grid_columnconfigure(0, weight=1)
lb2_fr1.grid_rowconfigure(2, weight=1)
lb2_fr1.grid_columnconfigure(0, weight=1)
lb3_fr1.grid_rowconfigure(3, weight=1)
lb3_fr1.grid_columnconfigure(0, weight=1)
lb4_fr1.grid_rowconfigure(4, weight=1)
lb4_fr1.grid_columnconfigure(0, weight=1)
#Configuração da Janela do 2º Frame:
lb1_fr2.grid_rowconfigure(1, weight=1)
lb1_fr2.grid_columnconfigure(0, weight=1)
lb2_fr2.grid_rowconfigure(2, weight=1)
lb2_fr2.grid_columnconfigure(0, weight=1)
lb3_fr2.grid_rowconfigure(2, weight=1)
lb3_fr2.grid_columnconfigure(3, weight=1)
lb4_fr2.grid_rowconfigure(1, weight=1)
lb4_fr2.grid_columnconfigure(5, weight=1)


#Loop
root.mainloop()

















