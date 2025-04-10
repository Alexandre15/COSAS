# PROCESSO DE OUTSIDE PEDIDO ABERTO

class outAberto:
    def __init__(self, item, quantidade, coleta, destino):
        self.item = item
        self.quantidade = quantidade
        self.coleta = coleta
        self.destino = destino


    def movimentarJob(item, quantidade):
        print("=-"*15)
        print(f"Movimentado o item: {item}")
        print(f"Quantidade: {quantidade}")
        print("=-"*15)
        return True


    def gerarNF(quantidade, volumes):
        print("Nota gerada")
        print(f"Quantidade: {quantidade}")
        print(f"Volumes: {volumes}")
        print("=-"*15)
        return True


    def solicitarFrete(coleta, destino):
        print(f"Coleta na {coleta} para entregar na {destino}")
        return True


    def cobrarMaterial(item, quantidade):
        print("Cobrar material dos processos anteriores")
        print(f"Cobrar planejador item {item} = {quantidade}")
        print("Solicitar prazo")
        print("Acompanhar entrega do processo anterior/planejador, para posterior envio")


    def temsaldo():
        saldo = str(input("O item que você analisou tem demanda e saldo? ( sim / não ): ")).lower()
        return saldo


def outsideAberto():
    print("=-"*40)
    print("Analisar shortage de OUTSIDE dentre os 90 PN quais tem demanda/saldo")
    print("=-"*40)

    saldo = outAberto.temsaldo()

    if saldo=="sim":
        print("Mandar para OUTSIDE")
        print("Solicitar movimentação física")
        if outAberto.movimentarJob(500, "3313867-SA") == True:
            if outAberto.gerarNF(500, 6) == True:
                outAberto.solicitarFrete("Eaton", "Grefortec")
                print("Acompanhar com fornecedor o prazo de retorno do material para planta, considerando o Lead time")
    else:
        print("Não temos saldo disponível")
        outAberto.cobrarMaterial(3313867, 500)
        retorno = str(input("Recebemos o material/dentro do prazo? (Sim, não): ")).lower()

        if retorno=="sim":
            print("Solicitar movimentação física")
            if outAberto.movimentarJob(500, "3313867-SA") == True:
                if outAberto.gerarNF(500, 6) == True:
                    outAberto.solicitarFrete("Eaton", "Grefortec")
                    print("Acompanhar com fornecedor o prazo de retorno do material para planta, considerando o Lead time")
        else:
            print("Escalonar/Sinalizar/Pedir ajuda")

outsideAberto()