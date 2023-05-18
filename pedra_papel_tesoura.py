jogadas = ["pedra", "papel", "tesoura"]
arquivo1 = open("CPUvsCPU.txt", "a")
arquivo2 = open("PLAYERvsCPU.txt", "a")
arquivo3 = open("PLAYERvsPLAYER.txt", "a")

import random
from getpass import getpass

    #CPU vs CPU

def cpu_cpu():
 print("Bem-vindo a CPU vs CPU")
 cpu1 = random.choice(jogadas)
 cpu2 = random.choice(jogadas)

 def determinar_vencedor(cpu1, cpu2):
     if cpu1 == cpu2:
        return "Empate"
     elif (cpu1 == "pedra" and cpu2 == "tesoura") or (cpu1 == "papel" and cpu2 == "pedra") or (cpu1 == "tesoura" and cpu2 == "papel"):
        return "CPU 1 venceu"
     else:
        return "CPU 2 venceu"

 resultado = determinar_vencedor(cpu1, cpu2)
 print(f"CPU 1 jogou {cpu1}")
 print(f"CPU 2 jogou {cpu2}")
 print(resultado)

 historico = "CPU1 colocou"+ " " + cpu1 + " " + "e a CPU2" + " " + cpu2 + " " + "entao deu" + " " + resultado + "."
 print(historico)
 arquivo1.write(historico + "\n")
 arquivo1.close()

    #PLAYER vs CPU

def player_cpu():
   
 print("Bem-vindo a PLAYER vs CPU")

 jogador = input("Escolha Pedra, papel ou tesoura: ").lower()
       
 computador = random.choice(jogadas)

 def determinar_vencedor(jogador, computador):
                       
    if jogador == computador:
        return "Empate"
    elif (jogador == "pedra" and  computador == "tesoura") or (jogador == "papel" and  computador == "pedra") or (jogador == "tesoura" and  computador == "papel"):
        return "Jogador venceu"
    else:
        return "Computador venceu"

 resultado = determinar_vencedor(jogador, computador)
 print(f"Jogador jogou {jogador}")
 print(f"CPU jogou {computador}")
 print(resultado)
       
 historico1 = "Jogador colocou"+ " " + jogador + " " + "e a CPU" + " " + computador + " " + "entao deu" + " " + resultado + "." 
 print(historico1)
 arquivo2.write(historico1 + "\n")
 arquivo2.close()


    #PLAYER vs PLAYER

def player_player():
 print("Bem-vindo a PLAYER vs PLAYER")

 jogador1 = getpass("Escolha Pedra, papel ou tesoura: ").lower()

 jogador2 = getpass("Escolha Pedra, papel ou tesoura: ").lower()

 def determinar_vencedor(jogador1, jogador2):                      
           
    if jogador1 == jogador2:
        return "Empate"
    elif (jogador1 == "pedra" and  jogador2 == "tesoura") or (jogador1 == "papel" and  jogador2 == "pedra") or (jogador1 == "tesoura" and  jogador2 == "papel"):
        return "Jogador 1 venceu"
    else:
        return "Jogador 2 venceu"

 resultado = determinar_vencedor(jogador1, jogador2)
 print(f"Jogador1 jogou {jogador1}")
 print(f"Jogador2 jogou {jogador2}")
 print(resultado)    
   
 historico2 = "Jogador1 colocou"+ " " + jogador1 + " " + "e o jogador2" + " " + jogador2 + " " + "entao deu" + " " + resultado + "."  
 print(historico2)
 arquivo3.write(historico2 + "\n")
 arquivo3.close()


    #HISTORICO

def historico():
    print("=======================================")
    print("* Modos:                              *")
    print("* 1 -> Apagar Historico CPUvsCPU      *")
    print("* 2 -> Olhar Historico  CPUvsCPU      *")
    print("* 3 -> Apagar Historico PLAYERvsPLAYER*")
    print("* 4 -> Olhar Historico  PLAYERvsPLAYER*")
    print("* 5 -> Apagar Historico PLAYERvsCPU   *")
    print("* 6 -> Olhar Historico  PLAYERvsCPU   *")
    print("=======================================")

    while True:    
     escolha = input("Escolha:")

     match escolha:
        case '1':
                arquivo1 = open("CPUvsCPU.txt", "w")
                print("Historico apagado")
                arquivo1.close
        case '2':
                print("Aqui está seu Historico:")
                arquivo1 = open("CPUvsCPU.txt", "r")
                ArquivosCompleto1 = arquivo1.read()
                print(ArquivosCompleto1)
        case '3':
                arquivo2 = open("PLAYERvsCPU.txt", "w")
                print("Historico apagado")
                arquivo2.close
        case '4':
                print("Aqui está seu Historico:")
                arquivo2 = open("PLAYERvsCPU.txt", "r")
                ArquivosCompleto2 = arquivo2.read()
                print(ArquivosCompleto2)
        case '5':
                arquivo3 = open("PLAYERvsPLAYER.txt", "w")
                print("Historico apagado")
                arquivo3.close
        case '6':
                print("Aqui está seu Historico:")
                arquivo3 = open("PLAYERvsPLAYER.txt", "r")
                ArquivosCompleto3 = arquivo3.read()
                print(ArquivosCompleto3)

print("==============================")
print("* Modos de jogo:             *")
print("* 1 -> Player vs CPU         *")
print("* 2 -> Player vs Player      *")
print("* 3 -> CPU vs CPU            *")
print("* 4 -> Historico             *")
print("==============================")

while True:
    mode = input("Escolha o modo:")
    if mode == '1':
       player_cpu()
       break
    elif mode == '2':
       player_player()
       break
    elif mode == '3':
        cpu_cpu()
        break
    elif mode == '3':
        cpu_cpu()
        break
    elif mode == '4':
        historico()
