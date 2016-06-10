import funcoes

despesasList = funcoes.recuperarDespesas()
receita = funcoes.recuperarReceita()

opcao = ""
while (opcao != "X"):
    funcoes.exibemenu()
    opcao = str.upper(input("Digite o número da sua opção: "))

    if opcao == "1":
     print("--------------- Renda familiar --------------")        
     receita = float(input("Digite o valor da receita: "))
     print ("Receita cadastrada!\n")

    elif opcao == "2":
       despesasList = funcoes.cadastroDespesas()
        
    elif opcao == "3":
        funcoes.listarDespesa(despesasList)


    elif opcao == "4":
        funcoes.excluirdespesa(despesasList)

    elif(opcao == "5"):
        soma = 0
        for i in range(len(despesasList)):
            soma += despesasList[i][1]

        if(receita - soma >= 0):
            print("Saldo Positivo!\nSaldo: R$" , receita - soma)
        else:
            print("Saldo Negativo!\nSaldo: R$" , receita - soma)
        
    elif(str.upper(opcao) == "X"):
        funcoes.salvarReceita(receita)
        funcoes.salvarDespesas(despesasList)
                
        
