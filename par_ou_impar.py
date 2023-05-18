import random
import time
from getpass import getpass

def logica_impar(num1, num2):
    if ((num1 + num2) % 2) == 0:
        
        print("Jogador 1 escolheu ", num1)
        
        time.sleep(0.5)
        print("Jogador 2 escolheu ", num2)
       
        time.sleep(0.5)
        print("Jogador 2 venceu")
        
        resultado = "Jogador 2 venceu"
        time.sleep(0.5)
        anotacao = ("Jogador 1 escolheu" + " " + str(num1) + " " + "/" + "Jogador 2 escolheu" + " " + str(num2) + " " + "/" + str(resultado))
        arq.write(str(anotacao))
        arq.write("\n")
        time.sleep(0.5)
        return(2)
    else:
        
        print("Jogador 1 escolheu ", num1)
        
        time.sleep(0.5)
        print("Jogador 2 escolheu ", num2)
       
        time.sleep(0.5)
        print("Jogador 1 venceu")
        
        resultado = "Jogador 1 venceu"
        time.sleep(0.5)
        anotacao = ("Jogador 1 escolheu" + " " + str(num1) + " " + "/" + "Jogador 2 escolheu" + " " + str(num2) + " " + "/" + str(resultado))
        arq.write(str(anotacao))
        arq.write("\n")
        time.sleep(0.5)
        return(1)
   


def logica_par(num1, num2):
    if ((num1 + num2) % 2) == 0:
        
        print("Jogador 1 escolheu ", num1)
       
        time.sleep(0.5)
        print("Jogador 2 escolheu ", num2)
       
        time.sleep(0.5)
        print("Jogador 1 venceu")
        
        resultado = "Jogador 1 venceu"
        time.sleep(0.5)
        anotacao = ("Jogador 1 escolheu" + " " + str(num1) + " " + "/" + "Jogador 2 escolheu" + " " + str(num2) + " " + "/" + str(resultado))
        arq.write(str(anotacao))
        arq.write("\n")
        time.sleep(0.5)

        return(1)
    else:
       
        print("Jogador 1 escolheu ", num1)
        
        time.sleep(0.5)
        print("Jogador 2 escolheu ", num2)
       
        time.sleep(0.5)
        print("Jogador 2 venceu")
        
        resultado = "Jogador 2 venceu"
        time.sleep(0.5)
        anotacao = ("Jogador 1 escolheu" + " " + str(num1) + " " + "/" + "Jogador 2 escolheu" + " " + str(num2) + " " + "/" + str(resultado))
        arq.write(str(anotacao))
        arq.write("\n")
        time.sleep(0.5)

        return(2)


while True:

    p1 = 0
    p2 = 0

    print(" ")
    print("******************************")
    print("* Bem vindo ao Impar/Par     *")
    print("* 1 -> Player vs CPU         *")
    print("* 2 -> Player vs Player      *")
    print("* 3 -> CPU vs CPU            *")
    print("* 4 -> Exibir historico      *")
    print("* 5 -> Limpar historico      *")
    print("* 6 -> Sair                  *")
    print("******************************")

    opcao = input()

    match opcao:
        case "1":
            while True:
                arq = open("ImparPar.txt", "a")
                print("****************************************")
                es = input("Escolha Impar (0) ou Par (1):\n""****************************************\n")
                print("****************************************")
                if  es == "0":
                    num1 = int(input("Digite um numero de 0 a 10:\n""****************************************\n"))
                    num2 = random.randint(0,10)
                    if logica_impar(num1, num2) == 1:
                        p1 += 1
                    else:
                        p2 += 1


                elif es == "1":
                    num1 = int(input("Digite um numero de 0 a 10:\n""****************************************\n"))
                    num2 = random.randint(0,10)
                    if logica_par(num1, num2) == 1:
                        p1 += 1
                    else:
                        p2 += 1
                   
                if p1 == 2:
                    print("****************************************")
                    print("Jogador 1 venceu o melhor de 3")
                elif p2 ==2:
                    print("****************************************")
                    print("Jogador 2 venceu o melhor de 3")

                if p1 == 2 or p2 == 2:
                    break

        case "2":
            while True:
                arq = open("ImparPar.txt", "a")
                print("****************************************")
                es = input("Escolha Impar (0) ou Par (1):\n""****************************************\n")
                print("****************************************")
                if  es == "0":
                    num1 = int(getpass("Digite um numero de 0 a 10:\n""****************************************\n"))
                    num2 = int(getpass("Digite um numero de 0 a 10:\n""****************************************\n"))
                    if logica_impar(num1, num2) == 1:
                        p1 += 1
                    else:
                        p2 += 1

                elif es == "1":
                    num1 = int(getpass("Digite um numero de 0 a 10:\n""****************************************\n"))
                    num2 = int(getpass("Digite um numero de 0 a 10:\n""****************************************\n"))
                    if logica_par(num1, num2) == 1:
                        p1 += 1
                    else:
                        p2 += 1
                       
                    if p1 == 2:
                        print("****************************************")
                        print("Jogador 1 venceu o melhor de 3")
                    elif p2 == 2:
                        print("****************************************")
                        print("Jogador 2 venceu o melhor de 3")

                    if p1 == 2 or p2 == 2:
                        break
        case "3":
            while True:
                arq = open("ImparPar.txt", "a")
                print("****************************************")
                es = random.choice(["0","1"])
                time.sleep(0.5)
                print("****************************************")
                if  es == "0":
                    num1 = random.randint(0,10)
                    time.sleep(0.5)
                    num2 = random.randint(0,10)
                    if logica_impar(num1, num2) == 1:
                        p1 += 1
                    else:
                        p2 += 1


                elif es == "1":
                    num1 = random.randint(0,10)
                    num2 = random.randint(0,10)
                    if logica_par(num1, num2) == 1:
                        p1 += 1
                    else:
                        p2 += 1
                           
                    if p1 == 2:
                        print("****************************************")
                        print("Jogador 1 venceu o melhor de 3")
                    elif p2 == 2:
                        print("****************************************")
                        print("Jogador 2 venceu o melhor de 3")

                    if p1 == 2 or p2 == 2:
                        break

        case "4":
            his = print("historico atual\n")
            arq = open("ImparPar.txt", "r")
            arquivo = arq.read()
            time.sleep(0.5)
            print(arquivo)
            arq.close
            time.sleep(1)
               
               
        case "5":
            hist = input("deseja apagar digite ""1:")
            
            arq = open("ImparPar.txt", "w")
            arq.close
               
              
        case "6":
            break