import random
import time
import os


class Color:
    violet = "\033[35m"
    red = "\u001b[31m"
    cyan = "\u001b[36m"
    green = "\u001b[32m"
    yellow = "\u001b[33m"
    fucsia = "\u001b[35;1m"
    gray = "\033[90m"
    reset = "\u001b[0m"


def cls():
    if os.name == 'nt':
        os.system("cls")
    else:
        os.system("clear")


def intro(tempo):
    cls()
    logo = [
        Color.green, 
        "           █   █ █▀▀█ █▀▀█ █▀▀▄ █   █▀▀",
        "           █▄█▄█ █  █ █▄▄▀ █  █ █   █▀▀",
        "            ▀ ▀  ▀▀▀▀ ▀ ▀▀ ▀▀▀  ▀▀▀ ▀▀▀",
        Color.gray,
        "  █▄▄ █▄█   ▄▀█ █   █▀▀ ▄▀█ █▄ █ █▀█ █ █ █ █▀ █▄▀ █",
        "  █▄█  █    █▀█ █▄▄ █▀  █▀█ █ ▀█ █▄█ ▀▄▀▄▀ ▄█ █ █ █",
        Color.reset,
    ]
    for i in logo:
        for j in i:
            print(j, end='', flush=True)
            if tempo:
                time.sleep(0.007)
        print()
    print("\n")


def selezione():
    with open("dictionary.txt", "r") as dizionario:
        parole = dizionario.readlines()
    estrazione = random.choice(parole)
    return estrazione.strip()


def validità(tentativo):
    with open("dictionary.txt", "r") as dizionario:
        parole = [line.strip() for line in dizionario.readlines()]
    if tentativo in parole:
        return True
    else:
        return False


def attemps(lista):
    for i in range(len(lista)):
        print("     ", Color.cyan, f'{i + 1}) ', Color.reset, end='')
        print(lista[i])
    

def indizi(parola1, parola2):
    finale = ""  
    fin = ['', '', '', '', '']
    temp = []
    for i in range(len(parola1)):
        if parola1[i] == parola2[i]:
            fin[i] = 'v'
            temp.append('4')
        else: 
            temp.append(parola2[i]) 
    for i in range(len(parola1)):
        if parola1[i] in temp:
            if fin[i] in temp:
                temp.remove(fin[i])
            fin[i] = 'g'
    parola1 = parola1.upper()
    for i in range(len(fin)):
        if fin[i] == 'v':
            finale += Color.green + parola1[i] + " "
        elif fin[i] == 'g':
            finale += Color.yellow + parola1[i] + " "
        else:
            finale += Color.reset + parola1[i] + " "
    return finale


def main():  
    intro(True)
    incognita = selezione()
    past = []
    for i in range(6):
        while True:
            intro(False)
            attemps(past)
            print("     ", Color.cyan, f'{i + 1}) ', Color.reset, end='')
            tentativo = input().lower()
            if validità(tentativo):
                colorato = indizi(tentativo, incognita)
                past.append(colorato)
                break
        if tentativo == incognita:
            break
    intro(False)
    attemps(past)
    print()
    print(Color.reset, "  Parola corretta -->", Color.violet, f'{incognita.upper()}', Color.reset)
    input()
    cls()
    

main()