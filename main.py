from tkinter import *

root = Tk()
root.title('Calculadora')
root.geometry('408x355')
root.minsize(408,355)
root.maxsize(408,355)

numero1 = ''
divisao = FALSE
multiplica = FALSE
soma = FALSE
subtracao = FALSE

root.configure(background='#240046')

e = Entry(root, width=15, borderwidth=4, relief=FLAT, fg='#FFFFFF', bg='#8500ff', font=('futura', 25, 'bold'), justify=CENTER)
e.grid(
    row=0,
    column=0,
    columnspan=4,
    pady=2 
)

#Funções Operadores

def botao_click(num):
    e.insert(END, num)
def botao_divisao():
    global numero1
    global divisao
    divisao = TRUE
    numero1 = e.get()
    e.delete(0, END)
def botao_multiplica():
    global numero1
    global multiplica
    multiplica = TRUE
    numero1 = e.get()
    e.delete(0, END)
def botao_subtracao():
    global numero1
    global subtracao
    subtracao = TRUE
    numero1 = e.get()
    e.delete(0, END)
def botao_soma():
    global numero1
    global soma
    soma = TRUE
    numero1 = e.get()
    e.delete(0, END)
def botao_limpa():
    e.delete(0, END)
def botao_igual():
    global subtracao
    global soma
    global multiplica
    global divisao
    numero2 = e.get()
    e.delete(0, END)
    if soma == TRUE:
        e.insert(0, int(numero1) + int(numero2))
        soma = FALSE
    if multiplica == TRUE:
        e.insert(0, int(numero1) * int(numero2))
        multiplica = FALSE
    if subtracao == TRUE:
        e.insert(0, int(numero1) - int(numero2))
        subtracao = FALSE
    if divisao == TRUE:
        e.insert(0, int(numero1) / int(numero2))
        divisao = FALSE


#Fileira do Divisor

divide = Button(root,
               text='÷',
               padx=40,
               pady=20,
               command=botao_divisao,
               fg='#FFFFFF',
               activeforeground='#FFFFFF',
               bg='#320064',
               activebackground='#240046',
               relief=FLAT,
               font=('futura', 12, 'bold')
)
divide.grid(row=0, column=4)

#Fileira da Multiplicação

multiplica = Button(root,
               text='×',
               padx=40,
               pady=20,
               command=botao_multiplica,
               fg='#FFFFFF',
               activeforeground='#FFFFFF',
               bg='#320064',
               activebackground='#240046',
               relief=FLAT,
               font=('futura', 12, 'bold')
)
multiplica.grid(row=1, column=4)

#Fileira da Subtração

subtracao = Button(root,
               text='–',
               padx=40,
               pady=20,
               command=botao_subtracao,
               fg='#FFFFFF',
               activeforeground='#FFFFFF',
               bg='#320064',
               activebackground='#240046',
               relief=FLAT,
               font=('futura', 12, 'bold')
)
subtracao.grid(row=2, column=4)

#Fileira da Soma

soma = Button(root,
               text='+',
               padx=40,
               pady=20,
               command=botao_soma,
               fg='#FFFFFF',
               activeforeground='#FFFFFF',
               bg='#320064',
               activebackground='#240046',
               relief=FLAT,
               font=('futura', 12, 'bold')
)
soma.grid(row=3, column=4)

#Fileira do igual

igual = Button(root,
               text='=',
               padx=40,
               pady=20,
               command=botao_igual,
               fg='#FFFFFF',
               activeforeground='#FFFFFF',
               bg='#320064',
               activebackground='#240046',
               relief=FLAT,
               font=('futura', 12, 'bold')
)
igual.grid(row=4, column=3)

#Fileira do botão 1

um = Button(root,
               text='1',
               padx=40,
               pady=20,
               command=lambda: botao_click(1),
               fg='#FFFFFF',
               activeforeground='#FFFFFF',
               bg='#320064',
               activebackground='#240046',
               relief=FLAT,
               font=('futura', 12, 'bold')
)
um.grid(row=3, column=1)

#Fileira do 2

dois = Button(root,
               text='2',
               padx=40,
               pady=20,
               command=lambda: botao_click(2),
               fg='#FFFFFF',
               activeforeground='#FFFFFF',
               bg='#320064',
               activebackground='#240046',
               relief=FLAT,
               font=('futura', 12, 'bold')
)
dois.grid(row=3, column=2)

#Fileira do 3

tres = Button(root,
               text='3',
               padx=40,
               pady=20,
               command=lambda: botao_click(3),
               fg='#FFFFFF',
               activeforeground='#FFFFFF',
               bg='#320064',
               activebackground='#240046',
               relief=FLAT,
               font=('futura', 12, 'bold')
)
tres.grid(row=3, column=3)

#Fileira do 4

quatro = Button(root,
               text='4',
               padx=40,
               pady=20,
               command=lambda: botao_click(4),
               fg='#FFFFFF',
               activeforeground='#FFFFFF',
               bg='#320064',
               activebackground='#240046',
               relief=FLAT,
               font=('futura', 12, 'bold')
)
quatro.grid(row=2, column=1)

#Fileira do 5

cinco = Button(root,
               text='5',
               padx=40,
               pady=20,
               command=lambda: botao_click(5),
               fg='#FFFFFF',
               activeforeground='#FFFFFF',
               bg='#320064',
               activebackground='#240046',
               relief=FLAT,
               font=('futura', 12, 'bold')
)
cinco.grid(row=2, column=2)

#Fileira do 6

seis = Button(root,
               text='6',
               padx=40,
               pady=20,
               command=lambda: botao_click(6),
               fg='#FFFFFF',
               activeforeground='#FFFFFF',
               bg='#320064',
               activebackground='#240046',
               relief=FLAT,
               font=('futura', 12, 'bold')
)
seis.grid(row=2, column=3)

#Fileira do 7

sete = Button(root,
               text='7',
               padx=40,
               pady=20,
               command=lambda: botao_click(7),
               fg='#FFFFFF',
               activeforeground='#FFFFFF',
               bg='#320064',
               activebackground='#240046',
               relief=FLAT,
               font=('futura', 12, 'bold')
)
sete.grid(row=1, column=1)

#Fileira do 8

oito = Button(root,
               text='8',
               padx=40,
               pady=20,
               command=lambda: botao_click(8),
               fg='#FFFFFF',
               activeforeground='#FFFFFF',
               bg='#320064',
               activebackground='#240046',
               relief=FLAT,
               font=('futura', 12, 'bold')
)
oito.grid(row=1, column=2)

#Fileira do 9

nove = Button(root,
               text='9',
               padx=40,
               pady=20,
               command=lambda: botao_click(9),
               fg='#FFFFFF',
               activeforeground='#FFFFFF',
               bg='#320064',
               activebackground='#240046',
               relief=FLAT,
               font=('futura', 12, 'bold')
)
nove.grid(row=1, column=3)

#Fileira do 0

zero = Button(root,
               text='0',
               padx=91,
               pady=20,
               command=lambda: botao_click(0),
               fg='#FFFFFF',
               activeforeground='#FFFFFF',
               bg='#320064',
               activebackground='#240046',
               relief=FLAT,
               font=('futura', 12, 'bold')
)
zero.grid(row=4, column=1, columnspan=2)

#Fileira do botão Limpar

limpa = Button(root,
               text='C',
               padx=38.5,
               pady=20,
               command=botao_limpa,
               fg='#FFFFFF',
               activeforeground='#FFFFFF',
               bg='#320064',
               activebackground='#240046',
               relief=FLAT,
               font=('futura', 12, 'bold')
)
limpa.grid(row=4, column=4)

root.mainloop()