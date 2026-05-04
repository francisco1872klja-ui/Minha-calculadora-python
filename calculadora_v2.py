while True:
    try:
        opcao = input ("Deseja calcular? S/N:").lower().strip() 
        if opcao == "n":
            print("Fechando...")
            break
        elif opcao == "s":
                        print("obrigado por calcular")
                        num1 = float (input("Digite um número:"))
                        escolha = input("Escolha a operação (+,-,*,/,%,**):")
                        num2 = float (input("Digite outro número:"))
                        if escolha == "+":
                            soma = num1 + num2
                            print(f"Resposta:{soma}")
                        elif escolha =="-":
                              subtracao = num1 - num2
                              print(f"Resposta:{subtracao}")
                        elif escolha == "*":
                              multiplicacao = num1 * num2
                              print(f"Resposta{multiplicacao}")
                        elif escolha == "/":
                              if num2 !=0:
                                    divisao = num1 / num2
                                    print(f"Resposta:{divisao}")
                              else:
                                    num2 = 0
                                    print("ERRO:não da zero!")
                        elif escolha == "%:":
                              porcentagem = num1 * num2 /100
                              print(f"Resposta:{porcentagem}")
                        elif escolha == "**":
                              Elevado = num1 ** num2
                              print(f"Resposta:{Elevado}")
    except ValueError:
          print("Coloque um número!")
          continue