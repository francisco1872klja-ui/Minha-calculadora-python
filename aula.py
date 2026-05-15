#Ler o comprimento de três retas
r1=float(input("Coloque uma reta:"))
r2=float(input("Outra reta:"))
r3=float(input("Outra reta:"))
#Regra da matemática + filtro
if r1+r2>r3 and r1+r3>r2 and r2+r3>r1:
    print("Sim, suas retas formam um triângulo!!")
else:
    print("Não, forma um triângulo!!")