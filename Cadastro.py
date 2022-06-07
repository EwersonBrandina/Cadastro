from tkinter import *
#Criando Janela e Frames
root = Tk()
root.title('Cadastro')
fr1 = Frame(root)
fr2 = Frame(root)
fr3 = Frame(root)
#Configuração da Janela:
#Configuração da Janela
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(2, weight=1)
root.grid_columnconfigure(0, weight=1)
#Label do 1º Frame:
lb0_fr1 = Label(fr1, text='Dados Pessoais', font='Arial 25')
lb1_fr1 = Label(fr1, text='Nome:', font='Arial 25')
lb2_fr1 = Label(fr1, text='Data Nasc.:', font='Arial 25')
lb3_fr1 = Label(fr1, text='CPF:', font='Arial 25')
lb4_fr1 = Label(fr1, text='Telefone:', font='Arial 25')
#Entry do 1º Frame:
in1_fr1 = Entry(fr1, font='Arial 25')
in2_fr1 = Entry(fr1, font='Arial 25')
in3_fr1 = Entry(fr1, font='Arial 25')
in4_fr1 = Entry(fr1, font='Arial 25')
#Posição dos Label do 1º Frame:
lb0_fr1.grid(row=0, column=0, sticky=NSEW)
lb1_fr1.grid(row=1, column=0, sticky=NSEW)
lb2_fr1.grid(row=2, column=0, sticky=NSEW)
lb3_fr1.grid(row=3, column=0, sticky=NSEW)
lb4_fr1.grid(row=4, column=0, sticky=NSEW)
#Posição dos Entry do 1º Frame:
in1_fr1.grid(row=1, column=1, sticky=NSEW)
in2_fr1.grid(row=2, column=1, sticky=NSEW)
in3_fr1.grid(row=3, column=1, sticky=NSEW)
in4_fr1.grid(row=4, column=1, sticky=NSEW)
#Label do 2º Frame:
lb0_fr2 = Label(fr2, text='Endereço', font='Arial 25')
lb1_fr2 = Label(fr2, text='Rua:', font='Arial 25')
lb2_fr2 = Label(fr2, text='Bairro:', font='Arial 25')
lb3_fr2 = Label(fr2, text='Cidade:', font='Arial 25')
lb4_fr2 = Label(fr2, text='Nº:', font='Arial 25')
lb5_fr2 = Label(fr2, text='UF:', font='Arial 25')
#Entry do 2º Frame:
in1_fr2 = Entry(fr2, font='Arial 25')
in2_fr2 = Entry(fr2, font='Arial 25')
in3_fr2 = Entry(fr2, font='Arial 25')
in4_fr2 = Entry(fr2, font='Arial 25')
in5_fr2 = Entry(fr2, font='Arial 25')
#Posição dos Label do 2º Frame:
lb0_fr2.grid(row=0, column=0, sticky=NSEW)
lb1_fr2.grid(row=1, column=0, sticky=NSEW)
lb2_fr2.grid(row=2, column=0, sticky=NSEW)
lb3_fr2.grid(row=2, column=2, sticky=NSEW)
lb4_fr2.grid(row=1, column=4, sticky=NSEW)
lb5_fr2.grid(row=2, column=4, sticky=NSEW)
#Posição dos Entry do 2º Frame:
in1_fr2.grid(row=1, column=1, sticky=NSEW)
in2_fr2.grid(row=2, column=1, sticky=NSEW)
in3_fr2.grid(row=2, column=3, sticky=NSEW)
in4_fr2.grid(row=1, column=5, sticky=NSEW)
in5_fr2.grid(row=2, column=5, sticky=NSEW)
#Criando dois buttons no 3º Frame:
bt0_fr3 = Button(fr3, text='Gravar Dados', font='Arial 25')
bt1_fr3 = Button(fr3, text='Listar Dados', font='Arial 25')
#Posição os buttons no 3º Frame:
bt0_fr3.grid(row=0, column=0, sticky=NSEW)
bt1_fr3.grid(row=0, column=1, sticky=NSEW)



#Pack
fr1.grid()
fr2.grid()
fr3.grid()
#Loop
root.mainloop()

















