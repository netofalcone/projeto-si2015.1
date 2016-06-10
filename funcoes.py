def somar (a,b):  
    print (a+b)

def exibemenu ():
    print("=======  Orçamento Familiar  ========")
    print("*                                   *")
    print("*[1] Receita familiar               *")
    print("*[2] Cadastrar despesas da Familia  *")
    print("*[3] Listar despesas                *")
    print("*[4] Remover despesas               *")
    print("*[5] Situação                       *")
    print("*[x] Sair                           *")
    print("=====================================")

def exibecategorias ():
    print("=======      CATEGORIAS      ========")
    print("                                     ")
    print("*[1] mercado                        *")
    print("*[2] energia                        *")
    print("*[3] água                           *")
    print("*[4] educação                       *")
    print("*[5] saúde                          *")
    print("*[6] vestiário                      *")
    print("*[7] transporte                     *")
    print("*[8] lazer                          *")
    print("*[9] extras                         *")
    print("=====================================")

def  cadastroDespesas():
    despesasList = []
    print("Cadastrar as despesas da familiar:/>")
    categorias = ["mercado","energia","água","educação","saúde","vestiário","transporte","lazer","extras"]
    for i in categorias:
        print("Gasto do " + i + ":")
        despesa = float(input("Digite o gasto: "))
        despesasList.append([i,despesa])
    print ("****Despesas cadastradas com sucesso, obrigado!****")
    return despesasList


def excluirdespesa(despesasList):
    exibecategorias ()
    categorias = ["mercado","energia","água","educação","saúde","vestiário","transporte","lazer","extras"]
    categoria = input("Digite a categoria que deseja excluir: ")

    while(categoria.lower() not in categorias):
        print("Categoria inválida!")
        print ("Digite o nome da categoria que deseja excluir.")
        exibecategorias ()
        categoria = input("Digite a categoria que deseja excluir: ")
        
    for i in range(len(despesasList)):
        if(despesasList[i][0] == categoria):
           del despesasList[i]
           break;

def listarDespesa(despesasList):
    for i in despesasList:
        contCaracter = len(i[0]) + len(str((i[1])))
        caracter = ("-"*(35-contCaracter))
        print(i[0], caracter, i[1] , "\n")

def salvarDespesas(despesasList):
    arquivo = open("Despesas.txt","w")
    for i in despesasList:
        arquivo.write(str(i[0])+"\n")
        arquivo.write(str(i[1])+"\n")
    arquivo.close()

def salvarReceita(saldo):
    arquivo = open("Receita.txt","w")
    arquivo.write(str(saldo)) 
    arquivo.close()

def recuperarDespesas():
    arquivosRecuperados = []
    arquivo = open("Despesas.txt","r")
    linha = arquivo.readline()
    linhaAux = arquivo.readline()
    
    while(len(linha) != 0):
        pacote = [linha[0:len(linha)-1] , float(linhaAux[0:len(linhaAux)-1])]
        arquivosRecuperados.append(pacote)
        linha = arquivo.readline()
        linhaAux = arquivo.readline()
    arquivo.close()
    return  arquivosRecuperados

def recuperarReceita():
    arquivo = open("Receita.txt","r")
    linha = arquivo.readline()
    arquivo.close()
    if(len(linha) != 0):
        print = linha[0:len(linha)-1]
        resultado = float(linha[0:len(linha)-1])
        return resultado
