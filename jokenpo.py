#Criar um sistema de random
import random
#criar uma lista random
jogo=["Pedra","Papel","Tesoura"]
opções=random.choice(jogo)
#Pedir para jogador colocar um objeto
objeto=str(input("Coloque Pedra,Papel,Tesoura:")).title()
#ver se o computador ou o jogador ganhou
if opções==objeto:
    print(f"Empate!!")
elif (objeto=="Pedra" and opções=="Tesoura")or(objeto=="Papel"and opções=="Pedra")or(objeto=="Tesoura"and opções=="Papel"):
    print(f"Computador {opções} \n Você {objeto} -Ganhou!!")
else:
    print(f" Computador {opções} \n Você {objeto} -Perdeu!!")