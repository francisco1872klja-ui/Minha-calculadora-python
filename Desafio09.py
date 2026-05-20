from random import randint
from time import sleep
tabela=("Pedra","Papel","Tesoura")
computador=randint(0,2)
print(" [0]Pedra \n [1]Papel \n [2]Tesoura")
jogador=int(input("Qual sua escolha:"))
print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PO!!")
print("-="*11)
print(f"Computador jogou {tabela[computador]}")
print(f"Jogador jogou {tabela[jogador]}")
print("-="*11)
if computador ==0:
    if jogador==0:
        print("Empate")
    elif jogador ==1:
        print("Jogador VENCEU!!")
    elif jogador==2:
        print("Computador VENCEU!!")
if computador==1:
    if jogador ==0:
        print("Computador VENCEU!!")
    elif jogador==1:
        print("Empate")
    elif jogador==2:
        print("Jogador VENCEU!!")
if computador==2:
    if jogador==0:
        print("Jogador VENCEU!!")
    elif jogador==1:
        print("Computador VENCEU!!")
    elif jogador==2:
        print("Empate")
if jogador not in tabela:
    print("Jogada invalida")
