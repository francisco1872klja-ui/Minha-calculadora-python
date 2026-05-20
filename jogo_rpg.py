import random
jogador=120
monstro=150
for i in range(5):
    dado_normal=random.randint(15,25)
    dado_critical=random.randint(10,50)
    dado_monstro=random.randint(5,25)
    dado_monstro_critcal=random.randint(20,30)
    print("Nova Rodada")
    escolha=input("Escolha:[1]Ataque normal | [2]Ataque Crítico:")
    if escolha =="1":
        monstro=monstro-dado_normal
        print(f"Você deu {dado_normal} de dano")
        print("Ataque do monstro!!")
        jogador=jogador-dado_monstro
        print(f"Ele te deu {dado_monstro} de dano")
    elif escolha =="2":
        monstro=monstro-dado_critical
        print(f"Você deu {dado_critical} de dano")
        print(f"Ataque do monstro Crítico!!")
        jogador=jogador-dado_monstro_critcal
        print(f"Ele te deu {dado_monstro_critcal} de dano")
    print(f"Vida do monstro:{monstro},\nVida do jogador:{jogador}")
if jogador>monstro:
    print("Você venceu o monstro!!")
elif jogador<monstro:
    print("O monstro te venceu!!")
elif jogador==monstro:
    print("Empate")
