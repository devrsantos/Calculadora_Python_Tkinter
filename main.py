from tkinter import *

root = Tk()
root.title("Calculadora")
root.geometry('408x335')
root.minsize(398,330)
root.maxsize(398,330)

grupo_1 = ''
divisao = FALSE
multiplica = FALSE
subtracao = FALSE
soma = FALSE

btm_background_color = '#265220'

root.configure(background='#282828')

enter = Entry(root, 
              width= 12,
              borderwidth= 4, 
              relief= FLAT, 
              fg= '#FFFFFF', 
              bg= '#a7a28f', 
              font= ('futura',25, 'bold'),
              justify=CENTER
              )

enter.grid(
    row= 0,
    column= 0,
    columnspan= 4,
    pady= 2
)

# Funções Operadores
def btn_click(num):
    enter.insert(END, num)

def btn_divisao():
    global grupo_1
    global divisao

    divisao = TRUE
    grupo_1 = enter.get()
    enter.delete(0, END)
    
def btn_multiplicacao():
    global grupo_1
    global multiplica

    multiplica = TRUE
    grupo_1 = enter.get()
    enter.delete(0, END)

def btn_subtracao():
    global grupo_1
    global subtracao

    subtracao = TRUE
    grupo_1 = enter.get()
    enter.delete(0, END)

def btn_adicao():
    global grupo_1
    global soma

    soma = TRUE
    grupo_1 = enter.get()
    enter.delete(0, END)

def btn_limpa():
    enter.delete(0, END)

def btn_total():
    global grupo_1
    global divisao
    global soma
    global subtracao
    global multiplica

    grupo_2 = enter.get()
    
    enter.delete(0, END)

    if soma == TRUE:
        total = int(grupo_1) + int(grupo_2)
        grupo_1 = total
        enter.insert(0, total)
        soma = FALSE
    
    if divisao == TRUE:
        total = int(grupo_1) / int(grupo_2)
        grupo_1 = total
        enter.insert(0, total)
        divisao = FALSE
    
    if multiplica == TRUE:
        total = int(grupo_1) * int(grupo_2)
        grupo_1 = total
        enter.insert(0, total)
        multiplica = FALSE

    if subtracao == TRUE:
        total = int(grupo_1) - int(grupo_2)
        grupo_1 = total
        enter.insert(0, total)
        subtracao = FALSE

btn_divide = Button(root,
    text= '÷',
    width= 1,
    padx= 40,
    pady= 20,
    command= lambda: btn_divisao(),
    fg= '#FFFFFF',
    activeforeground= '#FFFFFF',
    bg= btm_background_color,
    activebackground= btm_background_color,
    relief= FLAT,
    font= ('futura', 12, 'bold')
)

btn_divide.grid(row= 0, column= 4)

# Primeira Fileira
btn_um = Button(root,
    text= '1',
    padx= 40,
    pady= 20,
    command= lambda: btn_click(1),
    fg= '#FFFFFF',
    activeforeground= '#FFFFFF',
    bg= btm_background_color,
    activebackground= btm_background_color,
    relief= FLAT,
    font= ('futura', 12, 'bold')
)

btn_um.grid(row= 1, column= 1)

btn_dois = Button(root,
    text= '2',
    padx= 40,
    pady= 20,
    command= lambda: btn_click(2),
    fg= '#FFFFFF',
    activeforeground= '#FFFFFF',
    bg= btm_background_color,
    activebackground= btm_background_color,
    relief= FLAT,
    font= ('futura', 12, 'bold')
)

btn_dois.grid(row= 1, column= 2)

btn_tres = Button(root,
    text= '3',
    padx= 40,
    pady= 20,
    command= lambda: btn_click(3),
    fg= '#FFFFFF',
    activeforeground= '#FFFFFF',
    bg= btm_background_color,
    activebackground= btm_background_color,
    relief= FLAT,
    font= ('futura', 12, 'bold')
)

btn_tres.grid(row= 1, column= 3)

btn_multiplica = Button(root,
    text= 'x',
    width= 1,
    padx= 40,
    pady= 20,
    command= lambda: btn_multiplicacao(),
    fg= '#FFFFFF',
    activeforeground= '#FFFFFF',
    bg= btm_background_color,
    activebackground= btm_background_color,
    relief= FLAT,
    font= ('futura', 12, 'bold')
)

btn_multiplica.grid(row= 1, column= 4)

# Segunda Fileira
btn_quatro = Button(root,
    text= '4',
    padx= 40,
    pady= 20,
    command= lambda: btn_click(4),
    fg= '#FFFFFF',
    activeforeground= '#FFFFFF',
    bg= btm_background_color,
    activebackground= btm_background_color,
    relief= FLAT,
    font= ('futura', 12, 'bold')
)

btn_quatro.grid(row= 2, column= 1)

btn_cinco = Button(root,
    text= '5',
    padx= 40,
    pady= 20,
    command= lambda: btn_click(5),
    fg= '#FFFFFF',
    activeforeground= '#FFFFFF',
    bg= btm_background_color,
    activebackground= btm_background_color,
    relief= FLAT,
    font= ('futura', 12, 'bold')
)

btn_cinco.grid(row= 2, column= 2)

btn_seis = Button(root,
    text= '6',
    padx= 40,
    pady= 20,
    command= lambda: btn_click(6),
    fg= '#FFFFFF',
    activeforeground= '#FFFFFF',
    bg= btm_background_color,
    activebackground= btm_background_color,
    relief= FLAT,
    font= ('futura', 12, 'bold')
)

btn_seis.grid(row= 2, column= 3)

btn_subtrai = Button(root,
    text= '-',
    width= 1,
    padx= 40,
    pady= 20,
    command= lambda: btn_subtracao(),
    fg= '#FFFFFF',
    activeforeground= '#FFFFFF',
    bg= btm_background_color,
    activebackground= btm_background_color,
    relief= FLAT,
    font= ('futura', 12, 'bold')
)

btn_subtrai.grid(row= 2, column= 4)

# Terceira Fileira
btn_sete = Button(root,
    text= '7',
    padx= 40,
    pady= 20,
    command= lambda: btn_click(7),
    fg= '#FFFFFF',
    activeforeground= '#FFFFFF',
    bg= btm_background_color,
    activebackground= btm_background_color,
    relief= FLAT,
    font= ('futura', 12, 'bold')
)

btn_sete.grid(row= 3, column= 1)

btn_oito = Button(root,
    text= '8',
    padx= 40,
    pady= 20,
    command= lambda: btn_click(8),
    fg= '#FFFFFF',
    activeforeground= '#FFFFFF',
    bg= btm_background_color,
    activebackground= btm_background_color,
    relief= FLAT,
    font= ('futura', 12, 'bold')
)

btn_oito.grid(row= 3, column= 2)

btn_nove = Button(root,
    text= '9',
    padx= 40,
    pady= 20,
    command= lambda: btn_click(9),
    fg= '#FFFFFF',
    activeforeground= '#FFFFFF',
    bg= btm_background_color,
    activebackground= btm_background_color,
    relief= FLAT,
    font= ('futura', 12, 'bold')
)

btn_nove.grid(row= 3, column= 3)

btn_soma = Button(root,
    text= '+',
    width= 1,
    padx= 40,
    pady= 20,
    command= lambda: btn_adicao(),
    fg= '#FFFFFF',
    activeforeground= '#FFFFFF',
    bg= btm_background_color,
    activebackground= btm_background_color,
    relief= FLAT,
    font= ('futura', 12, 'bold')
)

btn_soma.grid(row= 3, column= 4)

# Quarta Fileira
btn_zero = Button(root,
    text= '0',
    padx= 90,
    pady= 20,
    command= lambda: btn_click(0),
    fg= '#FFFFFF',
    activeforeground= '#FFFFFF',
    bg= btm_background_color,
    activebackground= btm_background_color,
    relief= FLAT,
    font= ('futura', 12, 'bold')
)

btn_zero.grid(row= 4, column= 1, columnspan= 2)

btn_limpar = Button(root,
    text= 'C',
    padx= 39,
    pady= 20,
    command= lambda: btn_limpa(),
    fg= '#FFFFFF',
    activeforeground= '#FFFFFF',
    bg= btm_background_color,
    activebackground= btm_background_color,
    relief= FLAT,
    font= ('futura', 12, 'bold')
)

btn_limpar.grid(row= 4, column= 3)

btn_igual = Button(root,
    text= '=',
    padx= 40,
    pady= 20,
    command= lambda: btn_total(),
    fg= '#FFFFFF',
    activeforeground= '#FFFFFF',
    bg= btm_background_color,
    activebackground= btm_background_color,
    relief= FLAT,
    font= ('futura', 12, 'bold')
)

btn_igual.grid(row= 4, column= 4)

root.mainloop()

