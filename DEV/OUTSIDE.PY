from time import sleep
# PROCESSO DE OUTSIDE

# 1° Analise shortage

shortage = ["sertec", "javer", "usicol", "comsaldo", "semsaldo"]

def movimentarJob(qtd, item):
    print("=-"*15)
    print(f"Movimentado o item: {item}")
    print(f"Quantidade: {qtd}")
    print("=-"*15)
    return True


def gerarNF(qtd, volume):
    print("=-"*15)
    print("Nota gerada")
    print(f"Quantidade: {qtd}")
    print(f"Volumes: {volume}")
    print("=-"*15)
    return True


def solicitarFrete(coleta, destino):
    print(f"Coleta na {coleta} para entregar na {destino}")
    return True


def cobrarMaterial(item, qtd, data):
    print("Cobrar material dos processos anteriores")


for itens in shortage:
    if itens=="comsaldo":
        print("Mandar para OUTSIDE")
        if movimentarJob(500, "3313867-SA") == True:
            if gerarNF(500, 6) == True:
                solicitarFrete("Eaton", "Grefortec")
    else:
        print("Não temos saldo disponível")
