from tkinter import *
from tkinter import messagebox
from json import load
import json
import os
import os.path
import math


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

jan = Tk()
canvas = Canvas()

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
        
    nome = Label(canvas, text = "Nome: ", bg = "#a7b4c4", font=(None, 17))
    nome.place(x= 120, y = 120)
    
    nmr = Label(canvas, text = "Número de pinos: ", bg = "#a7b4c4", font=(None, 17))
    nmr.place(x= 120, y = 160)
    
    global nomeEnt
    nomeEnt = Entry(canvas)
    nomeEnt.bind("<KeyRelease>", nomeLim)
    nomeEnt.place(x = 200, y = 129)
    
    global nmrEnt
    nmrEnt = Entry(canvas)
    nmrEnt.bind("<KeyRelease>", numLim)
    nmrEnt.place(x = 323, y = 169)
    
    voltar = Button(canvas, text = "Voltar", command = lambda: [canvas.pack_forget(),
                                                                menu()],
                    bg = "#45429c", fg='white', height = 1, width = 8)
    voltar.place(x = 120, y = 340)
    
    nmrEnt.bind("<Return>", lambda event: [criaEnt(event, canvas)])
    
    
    canvas.create_rectangle(0, 0, 107, 107, fill = "#393b38")
    canvas.create_rectangle(0, 373, 107, 480, fill = "#393b38")
    canvas.create_rectangle(533, 0, 640, 107, fill = "#393b38")
    canvas.create_rectangle(533, 373, 640, 480, fill = "#393b38")
    
    canvas.create_rectangle(107, 107, 533, 373, fill = "#a7b4c4")
    
    canvas.pack(fill= BOTH, expand= True)


def nomeLim(event):
    ent = nomeEnt.get()
    
    if not(ent.isdigit()):
        nomeEnt.delete(len(ent) - 1, END);

def numLim(event):
    ent = nmrEnt.get()

    if (ent.isdigit()):
        if (int(ent) > 16):
            nmrEnt.delete(len(ent) - 1, END)
        if (len(ent) == 2 and int(ent) == 0):
            nmrEnt.delete(len(ent) - 1, END)
    else:
        nmrEnt.delete(len(ent) - 1, END)


def criaEnt(event, canvas):
    ent = nmrEnt.get()
    
    if (ent == "" or not ent.isdigit() or int(ent) > 16 or int(ent) == 0):
        return
        
    nmr = int(ent)
            
    if len(lstEnt):
        for i in range (0, len(lstEnt)):
            lstEnt[len(lstEnt)-1].destroy()
            lstEnt.pop(len(lstEnt)-1)

    if len(lstVal):
        for i in range (0, len(lstVal)):
            lstVal[len(lstVal)-1].destroy()
            lstVal.pop(len(lstVal)-1)
            
    labelVal = Label(canvas, text = "Valor dos pinos: ", bg = "#a7b4c4", font=(None, 17))
    labelVal.place(x= 120, y = 270)
    
    
    labelEnt = Label(canvas, text = "Entrada/Saída: ", bg = "#a7b4c4", font=(None, 17))
    labelEnt.place(x= 120, y = 200)
    
    for i in range (0, nmr):
        #print(i)
        lstEnt.append(Entry(canvas, width = 2))
    
    for i in range (0, nmr):
        
        lstVal.append(Entry(canvas, width = 2))
    
    for i in range (0, nmr):
        #print(i)
        lstEnt[i].place(x = 120 + i*20, y = 240)
        lstEnt[i].bind("<KeyRelease>", lambda event: limVal(event, 1))
        lstVal[i].place(x = 120 + i*20, y = 310)
        lstVal[i].bind("<KeyRelease>", lambda event: limVal(event, 0))
        
    ok = Button(canvas, text = "Salvar",  command = lambda: [dataSave(),
                                                             criaEnt(event, canvas)], bg = "#45429c",
                    fg='white', height = 1, width = 8)
    ok.bind
    ok.place(x = 447, y = 340)
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
    
    dados = []
    
    if (len(nomeEnt.get()) == 0):
        messagebox.showerror("Erro", "Erro no campo Nome. Por favor, inserir um valor válido")
        return
    
    dados = leBanco()
    
    pesquisa = checkEl(int(nomeEnt.get()))
    #print(pesquisa)
    
    
    if (len(nmrEnt.get()) == 0 or int(nmrEnt.get()) != len(lstVal)):
        messagebox.showerror("Erro", "Erro no campo Número de pinos. Por favor, inserir um valor válido")
        return
    
    if (len(valorPin) != len(lstVal)):
        messagebox.showerror("Erro", "Erro no campo Valor dos pinos. Por favor, preenche-lo totalmente")
        return
    
    if (len(entPin) != len(lstEnt)):
        messagebox.showerror("Erro", "Erro no campo Entrada. Por favor, preenche-lo totalmente")
        return
    
    if (pesquisa != None):
        messagebox.showerror("Erro", "Chip já cadastrado. Por favor, vá em editar o chip")
        return
        
        
    dicionario = {"Nome": int(nomeEnt.get()), "Numero": int(nmrEnt.get()), "Entrada": entPin, "Teste": [valorPin]}
    with open("dados.txt", 'w') as json_file:
        dados.append(dicionario)
        dados = sorted(dados, key = lambda x:x["Nome"])
        json.dump(dados, json_file, indent = 4, separators = (',', ': '))
    
    #print(nomeEnt.get())
    #print(nmrEnt.get())
    #print(entPin)
    #print(valorPin)

############################################################################
    
def telaBanco(canvas, jan, bias): #precisa implementar funcionalidade de carregamento, adicionar respostas para os botoes prox,anterior e editar
    iniBanco(jan)
    
    canvas = Canvas(jan, height = 810, width = 600, bg = "#575d6b")
    
    canvas.create_rectangle(0, 0, 80, 80, fill = "#393b38")
    canvas.create_rectangle(0, 730, 80, 810, fill = "#393b38")
    canvas.create_rectangle(520, 0, 600, 80, fill = "#393b38")
    canvas.create_rectangle(520, 730, 600, 810, fill = "#393b38")
    
    voltar = Button(canvas, text = "Voltar", command = lambda: [canvas.pack_forget(),
                                                                menu()],
                    bg = "#45429c", fg='white', height = 1, width = 8)
    voltar.place(x = 100, y = 695)
    
    canvas.create_rectangle(80, 80, 520, 730, fill = "#a7b4c4")
    
    canvas.pack(fill= BOTH, expand= True)
    loadBanco(canvas, bias)


def iniBanco(jan):
    jan.title("Banco de Chips")
    compJan = 600
    altJan = 810
    
    compTela = jan.winfo_screenwidth()
    altTela = jan.winfo_screenheight()
    
    jan.geometry(f'{compJan}x{altJan}+{int(compTela/2 - compJan / 2)}+{int(altTela/2 - altJan / 2)}')
    
    jan.resizable(False, False)
    
def loadBanco(canvas, bias):
    chips = leBanco()
    
    if not (len(chips)):
        aviso = Label(canvas, text = "Banco vazio", bg = "#a7b4c4", font=(None, 18))
        aviso.place(x= 300, y = 85 + 122, anchor = CENTER)        
    
    
    else :
        i = 0
        editar = []
        deletar = []
        for i in range((bias) * 5, 5 * (bias + 1)):
            if (i == len(chips)):
                break

            nomeBanco = Label(canvas, text = "Nome: ", bg = "#a7b4c4", font=(None, 13))
            nomeBanco.place(x= 100, y = 85 + (i%5)*122)
            
            pinoBanco = Label(canvas, text = "Número de pinos: ", bg = "#a7b4c4", font=(None, 13))
            pinoBanco.place(x= 100, y = 115 + (i%5)*122)
            
            nome = Label(canvas, text = chips[i]["Nome"], bg = "#a7b4c4", font=(None, 13))
            nome.place(x= 300, y = 85 + (i%5)*122)
            
            pinoBanco = Label(canvas, text = chips[i]["Numero"], bg = "#a7b4c4", font=(None, 13))
            pinoBanco.place(x= 300, y = 115 + (i%5)*122)
            
            editar.append(Button(canvas, text = "Detalhes", command = lambda i = i:  [canvas.pack_forget(),
                                                                              telaDetalhes(canvas, jan, i, 0)],
                        bg = "#45429c", fg='white', height = 1, width = 8))
            editar[i%5].place(x = 430, y = 85 + (i%5)*122)
            
            deletar.append(Button(canvas, text = "Deletar", command = lambda i = i:  [delChip(i, bias),
                                                                                  canvas.pack_forget()],
                        bg = "#45429c", fg='white', height = 1, width = 8))
            deletar[i%5].place(x = 430, y = 115 + (i%5)*122)
            
            i+=1
        
        if (len(chips) > 5 and bias != 0):
            antPag = Button(canvas, text = "Anterior", command = lambda:  [canvas.pack_forget(),
                            telaBanco(canvas, jan, bias - 1)],
                            bg = "#45429c", fg='white', height = 1, width = 8)
            antPag.place(x = 340, y = 695)
        
        
        
        if (len(chips) > 5 and bias != math.floor(len(chips)/5)):
            proxPag = Button(canvas, text = "Proxima", command = lambda: [canvas.pack_forget(),
                            telaBanco(canvas, jan, bias + 1)],
                             bg = "#45429c", fg='white', height = 1, width = 8)
            proxPag.place(x = 430, y = 695)
    

def leBanco():
    
    PATH = './dados.txt'
    
    if (os.path.isfile(PATH) and os.access(PATH, os.R_OK)):
        with open("dados.txt", 'r') as file:
            if (os.stat("dados.txt").st_size != 0):
                return json.load(file)
    return []

def checkEl(nome):
    chips = leBanco()
    #print(chips)
    #print(len(chips))
    
    if not (len(chips)):
        return None
    

    ini = 0
    fim = len(chips) - 1
    
    while(ini <= fim):
        
        meio = ((fim + ini)// 2)
        
        if nome > chips[meio]["Nome"]:
            ini = meio + 1
            #print(ini)
        elif nome < chips[meio]["Nome"]:
            fim = meio - 1
        else:
            return meio
    
    return None


    
    

############################################################################


def telaDetalhes(canvas, jan, ind, bias): #precisa implementar funcionalidade de carregamento, adicionar respostas para os botoes prox,anterior e editar
    iniDetalhes(jan)
    
    
    canvas = Canvas(jan, height = 810, width = 600, bg = "#575d6b")
    
    canvas.create_rectangle(0, 0, 80, 80, fill = "#393b38")
    canvas.create_rectangle(0, 730, 80, 810, fill = "#393b38")
    canvas.create_rectangle(520, 0, 600, 80, fill = "#393b38")
    canvas.create_rectangle(520, 730, 600, 810, fill = "#393b38")
    #print(ind)
    #print(math.floor(bias/5))
    
    voltar = Button(canvas, text = "Voltar", command = lambda: [canvas.pack_forget(),
                                                                telaBanco(canvas, jan, math.floor(ind/5))],
                    bg = "#45429c", fg='white', height = 1, width = 8)
    voltar.place(x = 100, y = 695)
    
    canvas.create_rectangle(80, 80, 520, 730, fill = "#a7b4c4")
    
    canvas.pack(fill= BOTH, expand= True)
    loadDetalhes(canvas, ind, bias)


def iniDetalhes(jan):
    jan.title("Detalhes do Chip")
    compJan = 600
    altJan = 810
    
    compTela = jan.winfo_screenwidth()
    altTela = jan.winfo_screenheight()
    
    jan.geometry(f'{compJan}x{altJan}+{int(compTela/2 - compJan / 2)}+{int(altTela/2 - altJan / 2)}')
    
    jan.resizable(False, False)
    

def loadDetalhes(canvas, ind, bias):
    chip = leBanco()[ind]
    
    titulo = "Chip " + str(chip["Nome"])
    label = Label(canvas, text = titulo,bg = "#a7b4c4", font=(None, 20))
    label.place(x= 300, y = 102, anchor=CENTER)
    
    print(ind)
    print(bias)
    
    deletar = []
    i = 0
    
    entsaiChip = Label(canvas, text = "Entrada/Saída: " + chip["Entrada"], bg = "#a7b4c4", font=(None, 13))
    entsaiChip.place(x= 300, y = 135, anchor=CENTER)
    
    for i in range((bias) * 5, 5 * (bias + 1)):
        if (i == len(chip["Teste"])):
            break
        
        testeChip = Label(canvas, text = "Teste: ", bg = "#a7b4c4", font=(None, 13))
        testeChip.place(x= 100, y = 155 + (i%5)*122)
        
        label = Label(canvas, text = chip["Teste"][i],bg = "#a7b4c4", font=(None, 13))
        label.place(x = 300, y = 155 + (i % 5)*122)
        
        deletar.append(Button(canvas, text = "Deletar", command = lambda i = i:  [delTeste(ind, i),
                                                                                  canvas.pack_forget()],
                        bg = "#45429c", fg='white', height = 1, width = 8))
        deletar[i%5].place(x = 430, y = 155 + (i%5)*122)
        
    print(i)
    editar = Button(canvas, text = "Editar", command = lambda i = i:  [iniEditar(ind)],
                    bg = "#45429c", fg='white', height = 1, width = 8)
    editar.place(x = 430, y = 90)
        
    if (len(chip["Teste"]) > 5 and bias != 0):
        antPag = Button(canvas, text = "Anterior", command = lambda:  [canvas.pack_forget(),
                        telaDetalhes(canvas, jan, ind, bias - 1)],
                        bg = "#45429c", fg='white', height = 1, width = 8)
        antPag.place(x = 340, y = 695)
    
    
    if (len(chip["Teste"]) > 5 and bias != math.floor(len(chip["Teste"])/5)):
        proxPag = Button(canvas, text = "Proxima", command = lambda: [canvas.pack_forget(),
                        telaDetalhes(canvas, jan, ind, bias + 1)],
                         bg = "#45429c", fg='white', height = 1, width = 8)
        proxPag.place(x = 430, y = 695)
    
    
############################################################################

def iniEditar(ind):
    tk2 = Toplevel()
    canvas2 = Canvas()
    
    tk2.title("Editar")
    compJan = 640
    altJan = 480
    
    compTela = tk2.winfo_screenwidth()
    altTela = tk2.winfo_screenheight()
    
    tk2.geometry(f"{compJan}x{altJan}+{int(compTela/2 - compJan / 2)}+{int(altTela/2 - altJan / 2)}")
    
    tk2.resizable(False, False)
    
    telaEditar(ind,canvas2, tk2)
    
def telaEditar(ind, canvas2, tk2):
    canvas2 = Canvas(tk2, height = 480, width = 640, bg = "#575d6b")
    
        
    canvas2.create_rectangle(0, 0, 107, 107, fill = "#393b38")
    canvas2.create_rectangle(0, 373, 107, 480, fill = "#393b38")
    canvas2.create_rectangle(533, 0, 640, 107, fill = "#393b38")
    canvas2.create_rectangle(533, 373, 640, 480, fill = "#393b38")
    
    canvas2.create_rectangle(107, 107, 533, 373, fill = "#a7b4c4")
    
    canvas2.pack(fill= BOTH, expand= True)
    
    label = Label(canvas2, text = "Adicionar Teste", bg = "#a7b4c4", font=(None, 20))
    label.place(x= 320, y = 140, anchor=CENTER)
    
    loadEditar(ind, tk2, canvas2)
    
def loadEditar(ind, tk2, canvas2):
    chip = leBanco()[ind]
    
    if len(lstVal):
        for i in range (0, len(lstVal)):
            lstVal[len(lstVal)-1].destroy()
            lstVal.pop(len(lstVal)-1)
            
    for i in range (0, chip["Numero"]):
        lstVal.append(Entry(canvas2, width = 2))
        lstVal[i].place(x = 120 + i*20, y = 200)
        lstVal[i].bind("<KeyRelease>", lambda event: limVal(event, 0))
        
    voltar = Button(tk2, text = "Voltar", command = lambda: [tk2.destroy()],
                    bg = "#45429c", fg='white', height = 1, width = 8)
    voltar.place(x = 120, y = 340)
    
    addTeste = Button(tk2, text = "Adicionar", command = lambda:  [saveEditar(ind),
                                                                    telaEditar(ind, tk2, canvas2)
                                                                   ], bg = "#45429c", fg='white', height = 1, width = 8)
    addTeste.bind
    addTeste.place(x = 447, y = 340)
    
    
def saveEditar(ind):
    
    dados = []
    dados = leBanco()
    
    if (len(valorPin) != len(lstVal)):
        messagebox.showerror("Erro", "Erro no campo Valor dos pinos. Por favor, preenche-lo totalmente")
        return
    
    dicionario = dados[ind]
    dados.pop(ind)
    print(dicionario)
    dicionario["Teste"].append(valorPin)

    
    with open("dados.txt", 'w') as json_file:
        dados.append(dicionario)
        dados = sorted(dados, key = lambda x:x["Nome"])
        json.dump(dados, json_file, indent = 4, separators = (',', ': '))

############################################################################

def delChip(i, bias):
    chips = leBanco()
    
    chips.pop(i)
    
    with open("dados.txt", 'w') as json_file:
        chips = sorted(chips, key = lambda x:x["Nome"])
        json.dump(chips, json_file, indent = 4, separators = (',', ': '))
    
    if (i % 5 == 0 and i != 0):
        telaBanco(canvas, jan, bias - 1)
        
    telaBanco(canvas, jan, bias)
    

def delTeste(ind, i):
    chips = leBanco()
    
    dicionario = chips[ind]
    chips.pop(ind)
    dicionario["Teste"].pop(i)
    
    with open("dados.txt", 'w') as json_file:
        if (len(dicionario["Teste"]) > 0):
            chips.append(dicionario)
            
        chips = sorted(chips, key = lambda x:x["Nome"])
        json.dump(chips, json_file, indent = 4, separators = (',', ': '))
        
    if (len(dicionario["Teste"]) > 0):
        if (i % 5 == 0 and i != 0):
            telaDetalhes(canvas, jan, ind, i//5 - 1)
        else:
            telaDetalhes(canvas, jan, ind, i//5)
    else:
        telaBanco(canvas, jan, 0)
        

############################################################################



def menu():
    iniWnd()
    
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
                                                                  telaBanco(canvas, jan, 0)], bg = "#45429c",
                    fg='white', height = 1, width = 8)
    botao2.place(x = 280, y = 220)
    
    canvas.pack(fill= BOTH, expand= True)
    
   

def iniWnd():
    jan.title("Menu Inicial")
    compJan = 480
    altJan = 360
    
    compTela = jan.winfo_screenwidth()
    altTela = jan.winfo_screenheight()
    
    jan.geometry(f'{compJan}x{altJan}+{int(compTela/2 - compJan / 2)}+{int(altTela/2 - altJan / 2)}')
    
    jan.resizable(False, False)	
