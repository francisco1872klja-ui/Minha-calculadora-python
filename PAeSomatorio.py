#pegar as informações da PA
a1=int(input("Coloque o primeiro termo:"))
n=int(input("Coloque a quantidadde de termo:"))
r=int(input("Coloque a razão:"))
#perguntar se ele sabe o ultimo termo
sabe=input("\033[34mVocê sabe o último termo?(s/n)").upper()
if sabe =="S":
    an=input("Qual é o último termo:")
#fazer a conta
else:
#se n souber calcula sozinho
    an=a1+(n-1)*r
print(f"O programa calculou o último termo é {an}")
soma=((a1+an)*n)/2
print(f"A soma dos termos dessa PA é {soma}")