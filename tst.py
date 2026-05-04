while True:
    try:
            opcao=input("Deseja fazer um calculo?(s/n)")
            if opcao == "n":
                break
            else: 
                if opcao == "s":
                    print("obrigado por calcular")
                num1 = float (input("Digite um número:")) 
                operacao = input("Digite a operação +,-,* ,/,%,**:").strip()
                num2 = float (input("Digite outro numero:"))
                if operacao == "+":
                    soma = num1 + num2 
                    print(f"Resultado da soma:{soma}")
                elif operacao == "-":
                    subtracao = num1 - num2 
                    print(f"Resultado da subtração:{subtracao}")
                elif operacao == "*":
                    multiplicacao = num1 * num2
                    print(f"Resultado é:{multiplicacao}")
                elif operacao =="/":
                    if num2 !=0:
                        divisao = num1 / num2
                        print(f"Resultado é:{divisao}")
                    else:
                        print("ERRO:Divisão por zero não é permitida")
                elif operacao == "%":
                    porcentagem = num1 * num2 / 100
                    print(f"Resposta:{porcentagem}")
                elif operacao =="**":
                    Elevado = num1 ** num2
                    print(f"Resposta é:{Elevado}")
                else:
                    print(f"Inreal:{operacao}")
    except ValueError:
            print("ERROR:PorFavor coloque um Número")
            continue