def dimensoesObjeto():
    loop = int(1)
    while loop == 1: #Inicia o loop para garantir que o valor recebido irá ser válido dentro das dimensões da empresa
        while True:
            try:
                a = float(input("Diga a altura do objeto em cm: ")) #Define variavel a(altura) e faz o pedido da altura do objeto em float
                break
            except ValueError: #Retorna para o try caso seja encontrada 
                print("Você digitou a altura do objeto com valor não numérico")
        while True:
            try:
                b = float(input("Diga a largura do objeto em cm: ")) #Define a variavel b(largura) e faz o pedido da largura do objeto em float
                break
            except ValueError: #Retorna para o try caso seja encontrada falha na entrada de valor
                    print("Você digitou a largura do objeto com valor não numérico")
        while True:
                try:
                    c = float(input("Diga o comprimento do objeto em cm: ")) #Define variavel c(comprimento) e faz o pedido da altura do objeto em float
                    break
                except ValueError: #Retorna para o try caso seja encontrada falha na entrada de valor
                        print("Você digitou o comprimento do objeto com valor não numérico")
        d = a*b*c #Faz o calculo do volume do objeto
        if d > 0 and d < 1000:
            e = float(10) #Define que o valor respectivo ao volume do objeto é de R$ 10,00
            print("O valor é R$ 10,00")
            loop = 0 #Encerra o loop
        elif d >= 1000 and d < 10000:
            e = float(20) #Define que o valor respectivo ao volume do objeto é de R$ 20,00
            print("O valor é R$ 20,00")
            loop = 0 #Encerra o loop
        elif d >= 10000 and d < 30000:
            e = float(30) #Define que o valor respectivo ao volume do objeto é de R$ 30,00
            print("O valor é R$ 30,00")
            loop = 0 #Encerra o loop
        elif d >= 30000 and d < 100000:
            e = float(50) #Define que o valor respectivo ao volume do objeto é de R$ 50,00
            print("O valor é R$ 50,00")
            loop = 0 #Encerra o loop
        else:
            print("Não aceitamos objetos com dimensões tão grandes")
            continue #Volta ao inicio do loop porque o objeto tinha dimensão grande demais
        return e

def pesoObjeto():
    po = float(-5)
    loop = int(1)
    while loop == 1:
        while True: #Inicio do loop para garantir que o objeto não é pesado demais para as especificações da empresa
            try: #Try para evitar que o valor digitado seja não numérico
                po = float(input("Diga o peso do objeto em kg: ")) #Define variavel po(peso objeto) e pede entrada de um número em float(caso de numeros como 0.5kg)
                break #Encerra o try visto que foi inserido um número
            except ValueError: #Retorna para o try caso seja encontrada falha na entrada de valor
                print("Você digitou o peso do objeto com valor não numérico. ")
                continue #Volta ao try porque não foi inserido um numero
        if po <= 0.1:
            mpo = 1 #Define que o multiplicador do peso do objeto(mpo) será 1
            print("O multiplicador é 1")
            loop = 0
        elif po > 0.1 and po <= 1:
            mpo = 1.5 #Define que o multiplicador do peso do objeto(mpo) será 1.5
            print("O multiplicador é 1.5")
            loop = 0
        elif po > 1 and po <= 10:
            mpo = 2 #Define que o multiplicador do peso do objeto(mpo) será 2
            loop = 0
            print("O multiplicador é 2")
        elif po > 10 and po <= 30:
            mpo = 3 #Define que o multiplicador do peso do objeto(mpo) será 3
            print("O multiplicador é 3")
            loop = 0
        else:
            print("Objeto muito pesado, encomenda não aceita.")
            continue
    return mpo

def rotaObjeto():
    loop = int(1)
    while loop == 1: #Inicio do loop para garantir que a rota será válida
        rota = input("RS - De Rio de Janeiro até São Paulo\nBS - De Brasília até São Paulo\nRB - Rio de Janeiro até Brasília\nDiga a rota: ") #Define variável rota e pede entrada de uma das rotas listadas
        if rota == 'RS' or rota == 'rs': #if para escolha da rota RS/rs
            pr = 1 #Define que o multiplicador de preço da rota será 1
            loop = 0 #Encerra o loop
        elif rota == 'BS' or rota == 'bs': #if para escolha da rota BS/bs
            pr = 1.2 #Define que o multiplicador de preço da rota será 1.2
            loop = 0 #Encerra o loop
        elif rota == 'RB' or rota == 'rb': #if para escolha da rota RB/rb
            pr = 1.5 #Define que o multiplicador de preço da rota será 1.5
            loop = 0 #Encerra o loop
        else:
            print("Você digitou uma rota que não existe")
            continue #Volta ao inicio do loop porque a rota não é existente nas especificações da empresa
    return pr
            
#Programa principal
g, l, m, = -1, -1, -1 #Cria variaveis para receberem retorno
pt = float #Cria variavel do preço total
print("Bem vindo a Companhia de Logistica de Entregas")
g = dimensoesObjeto() #Variavel g recebe retorno da função dimensoesObjeto
l = pesoObjeto() #Variavel l recebe retorno da função pesoObjeto
m = rotaObjeto() #Variavel m recebe retorno da função rotaObjeto
pt = g*l*m #Calcula o preço total baseado em dimensões*peso*rota
print("Total a pagar(R$): {:.2f} (dimensões: {:.0f} * peso {:.1f} * rota {:.1f})" .format(pt, g, l, m))
