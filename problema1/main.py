import json

def importaDados():
    with open("problema1/data.json", encoding="UTF-8") as arquivo:
        dados = json.load(arquivo)
    return dados

def calculaComissao():
    dados = importaDados()
    totaisComissao = {}
    for item in dados["vendas"]:
        if item["valor"]<100:
            item["valor"]=0 
        if item["valor"]>=100 and item["valor"]<500:
            item["valor"] = item["valor"]/100
        if item["valor"]>=500:
            item["valor"]= item["valor"]*(5/100)
        totaisComissao[item["vendedor"]] = totaisComissao.get(item["vendedor"], 0) + item["valor"]

    return(totaisComissao)

def main():
    totais = calculaComissao()
    for vendedor, total in totais.items():
        print(f"{vendedor}: R$ {total:.2f}")


if __name__ == "__main__":
    main()
