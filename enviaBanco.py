from serial import Serial
from json import load
import json
import os.path


def envia():
    meu_serial = Serial("/dev/serial0", baudrate=9600, timeout=0.01)
    
    PATH = "./dados.txt"
    
    if (os.path.isfile(PATH) and os.access(PATH, os.R_OK)):
        with open("dados.txt", 'r') as file:
            if (os.stat("dados.txt").st_size != 0):
                chips = json.load(file)
                for x in range(0, len(chips)):
                    chip = "chip"
                    nome = str(chips[x]["Nome"])
                    totalP = str(chips[x]["Numero"])
                    entrada = chips[x]["Entrada"]
                    totalT= str(len(chips[x]["Teste"]))
                    
                    texto = " ".join([chip, nome, totalP, entrada, totalT]) + "\n"
                    meu_serial.write(texto.encode("UTF-8"))
                    
                    for y in range(0, len(chips[x]["Teste"])):
                        textoTeste = "teste " + chips[x]["Teste"][y] + "\n"
                        meu_serial.write(textoTeste.encode("UTF-8"))
                    
    return
