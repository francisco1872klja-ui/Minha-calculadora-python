#pedir o nome eo lv
nome=input("Coloque seu nome:").title()
lv=input("Coloque seu level:")
#comparar os niveis e mostrar sua categoria
if nome =="":
    print("Coloque um nome pfv!!")
elif lv=="":
    print("Coloque um lvl pfv!!")
elif not lv.isdigit():
    print("Coloque ápenas número!!")
else:
    level=int(lv)
    if level <10:
        print("\033[30mIniciante\033[m!!")
    elif level >=10 and level<=39:
        print("\033[33mVeterano\033[m!!")
    elif level>40:
         print("\033[34mPro-player\033[m!!")