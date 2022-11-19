from tkinter import *
from tkinter import messagebox


global lstVal
lstVal = []

global lstEnt
lstEnt = []

global nmrEnt
nmrEnt = 0

global valorPin
valorPin = ""

global entPin
entPin = ""

def iniAdd(jan):      
    jan.title("Adicionar")
    compJan = 640
    altJan = 480
    
    compTela = jan.winfo_screenwidth()
    altTela = jan.winfo_screenheight()
    
    jan.geometry(f"{compJan}x{altJan}+{int(compTela/2 - compJan / 2)}+{int(altTela/2 - altJan / 2)}")
    
    jan.resizable(False, False)
   
   
   
def telaAdd(canvas, jan):
    iniAdd(jan)
    
    
    
    canvas = Canvas(jan, height = 480, width = 640, bg = "#575d6b")
        
    nome = Label(canvas, text = "Nome: ", bg = "#a7b4c4", font=(None, 40))
    nome.place(x= 120, y = 120)
    
    nmr = Label(canvas, text = "Número de pinos: ", bg = "#a7b4c4", font=(None, 40))
    nmr.place(x= 120, y = 160)
    
    global nomeEnt
    nomeEnt = Entry(canvas)
    nomeEnt.place(x = 200, y = 129)
    
    voltar = Button(canvas, text = "Voltar", command = lambda: [canvas.pack_forget(),
                                                                menu(canvas, jan)],
                    bg = "#45429c", fg='white', height = 1, width = 8)
    voltar.place(x = 120, y = 340)
    
    global nmrEnt
    nmrEnt = Entry(canvas)
    nmrEnt.bind("<KeyRelease>", numEnt)
    nmrEnt.bind("<Return>", lambda event: criaEnt(event, canvas))
    nmrEnt.place(x = 323, y = 169)
    
    
    canvas.create_rectangle(0, 0, 107, 107, fill = "#393b38")
    canvas.create_rectangle(0, 373, 107, 480, fill = "#393b38")
    canvas.create_rectangle(533, 0, 640, 107, fill = "#393b38")
    canvas.create_rectangle(533, 373, 640, 480, fill = "#393b38")
    
    canvas.create_rectangle(107, 107, 533, 373, fill = "#a7b4c4")
    
    canvas.pack(fill= BOTH, expand= True)


def numEnt(event):
    ent = nmrEnt.get()

    if (ent.isdigit()):
        if (int(ent) > 20):
            nmrEnt.delete('0', END)
        if (len(ent) == 2 and int(ent) == 0):
            nmrEnt.delete('0', END)
    else:
        nmrEnt.delete('0', END)


def criaEnt(event, canvas):
    ent = nmrEnt.get()
    
    if (ent == "" or not ent.isdigit() or int(ent) > 20 or int(ent) == 0):
        return
        
    nmr = int(ent)
    
    if len(lstVal):
        for i in range (0, len(lstVal)):
            #print(i)
            lstVal[0].place_forget()
            lstEnt[0].place_forget()
            lstVal.pop(0)
            lstEnt.pop(0)
            
    labelVal = Label(canvas, text = "Valor dos pinos: ", bg = "#a7b4c4", font=(None, 40))
    labelVal.place(x= 120, y = 200)
    
    
    labelEnt = Label(canvas, text = "Entrada: ", bg = "#a7b4c4", font=(None, 40))
    labelEnt.place(x= 120, y = 270)
    
    ok = Button(canvas, text = "Salvar", command = dataSave, bg = "#45429c",
                    fg='white', height = 1, width = 8)
    ok.place(x = 447, y = 340)
    
    for i in range (0, nmr):
        #print(i)
        lstVal.append(Entry(canvas, width = 2))
        lstEnt.append(Entry(canvas, width = 2))
    
    for i in range (0, nmr):
        #print(i)
        lstVal[i].place(x = 120 + i*20, y = 240)
        lstVal[i].bind("<KeyRelease>", lambda event: limVal(event, 0))
        lstEnt[i].place(x = 120 + i*20, y = 310)
        lstEnt[i].bind("<KeyRelease>", lambda event: limVal(event, 1))
    #print(len(lstVal))

def limVal(event, tipo):
    if (tipo == 0):
        #print("")
        global valorPin
        valorPin = ""
        for el in lstVal:
            
            val = el.get()
            if (len(val) == 2 or not val.isdigit() or (int(val) != 0 and int(val) != 1)):
                el.delete('0', END)
            else:
                valorPin += val
                #print(valorPin)
    else:
        #print("")
        global entPin
        entPin= ""
        for el in lstEnt:
            
            ent = el.get()
            if (len(ent) == 2 or not ent.isdigit() or (int(ent) != 0 and int(ent) != 1)):
                el.delete('0', END)
            else:
                entPin += ent


def dataSave(): #falta inserir no banco, porém é funcional
    
    if (len(nomeEnt.get()) == 0):
        messagebox.showerror("Erro", "Erro no campo Nome. Por favor, inserir um valor válido")
        return
    
    if (len(nmrEnt.get()) == 0 or int(nmrEnt.get()) != len(lstVal)):
        messagebox.showerror("Erro", "Erro no campo Número de pinos. Por favor, inserir um valor válido")
        return
    
    if (len(valorPin) != len(lstVal)):
        messagebox.showerror("Erro", "Erro no campo Valor dos pinos. Por favor, preenche-lo totalmente")
        return
    
    if (len(entPin) != len(lstEnt)):
        messagebox.showerror("Erro", "Erro no campo Entrada. Por favor, preenche-lo totalmente")
        return
        
    print(nomeEnt.get())
    print(nmrEnt.get())
    print(entPin)
    print(valorPin)

############################################################################
    
def telaBanco(canvas, jan): #precisa implementar funcionalidade de carregamento, adicionar respostas para os botoes prox,anterior e editar
    iniBanco(jan)
    
    canvas = Canvas(jan, height = 810, width = 600, bg = "#575d6b")
    
    canvas.create_rectangle(0, 0, 80, 80, fill = "#393b38")
    canvas.create_rectangle(0, 730, 80, 810, fill = "#393b38")
    canvas.create_rectangle(520, 0, 600, 80, fill = "#393b38")
    canvas.create_rectangle(520, 730, 600, 810, fill = "#393b38")
    
    for i in range (0, 5):
    
        nomeBanco = Label(canvas, text = "Nome: ", bg = "#a7b4c4", font=(None, 30))
        nomeBanco.place(x= 100, y = 85 + i*122)
        
        pinoBanco = Label(canvas, text = "Número de pinos: ", bg = "#a7b4c4", font=(None, 30))
        pinoBanco.place(x= 100, y = 115 + i*122)
        
        valBanco = Label(canvas, text = "Valor dos pino: ", bg = "#a7b4c4", font=(None, 30))
        valBanco.place(x= 100, y = 145 + i*122)
        
        entBanco = Label(canvas, text = "Entrada: ", bg = "#a7b4c4", font=(None, 30))
        entBanco.place(x= 100, y = 175 + i*122)
        
        editar = Button(canvas, text = "editar", command = lambda: None,
                    bg = "#45429c", fg='white', height = 1, width = 8)
        editar.place(x = 430, y = 85 + i*122)
    
    voltar = Button(canvas, text = "Voltar", command = lambda: [canvas.pack_forget(),
                                                                menu(canvas, jan)],
                    bg = "#45429c", fg='white', height = 1, width = 8)
    voltar.place(x = 100, y = 695)
    
    
    
    antPag = Button(canvas, text = "Anterior", command = lambda: None,
                    bg = "#45429c", fg='white', height = 1, width = 8)
    antPag.place(x = 340, y = 695)
    
    
    
    proxPag = Button(canvas, text = "Proxima", command = lambda: None,
                     bg = "#45429c", fg='white', height = 1, width = 8)
    proxPag.place(x = 430, y = 695)
    
    
    
    canvas.create_rectangle(80, 80, 520, 730, fill = "#a7b4c4")
    
    canvas.pack(fill= BOTH, expand= True)


def iniBanco(jan):
    jan.title("Banco de Chips")
    compJan = 600
    altJan = 810
    
    compTela = jan.winfo_screenwidth()
    altTela = jan.winfo_screenheight()
    
    jan.geometry(f'{compJan}x{altJan}+{int(compTela/2 - compJan / 2)}+{int(altTela/2 - altJan / 2)}')
    
    jan.resizable(False, False)	

############################################################################



def menu(canvas, jan):
    iniWnd(jan)
    
    canvas = Canvas(jan, height = 360, width = 480, bg = "#575d6b")
    
    label = Label(canvas, text = "IC TESTER", bg = "#a7b4c4", font=(None, 40))
    label.place(x= 240, y = 120, anchor=CENTER)
    
    canvas.create_rectangle(0, 0, 80, 80, fill = "#393b38")
    canvas.create_rectangle(0, 280, 80, 360, fill = "#393b38")
    canvas.create_rectangle(400, 0, 480, 80, fill = "#393b38")
    canvas.create_rectangle(400, 280, 480, 360, fill = "#393b38")
    
    canvas.create_rectangle(80, 80, 400, 280, fill = "#a7b4c4")
    
    botao = Button(canvas, text = "Adicionar", command = lambda: [canvas.pack_forget(),
                                                                  telaAdd(canvas, jan)],
                   bg = "#45429c", fg='white', height = 1, width = 8)
    botao.place(x = 130, y = 220)
    
    botao2 = Button(canvas, text = "Ver Banco", command = lambda: [canvas.pack_forget(),
                                                                  telaBanco(canvas, jan)], bg = "#45429c",
                    fg='white', height = 1, width = 8)
    botao2.place(x = 280, y = 220)
    
    canvas.pack(fill= BOTH, expand= True)
    
   

def iniWnd(jan):
    jan.title("Menu Inicial")
    compJan = 480
    altJan = 360
    
    compTela = jan.winfo_screenwidth()
    altTela = jan.winfo_screenheight()
    
    jan.geometry(f'{compJan}x{altJan}+{int(compTela/2 - compJan / 2)}+{int(altTela/2 - altJan / 2)}')
    
    jan.resizable(False, False)	
