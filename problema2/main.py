import json
import sys

ARQUIVO = "problema2/data.json"


def registrar_entrada(dados):
    try:
        codigo = int(input("Código do produto: "))
        qtde = int(input("Quantidade de entrada: "))
    except ValueError:
        print("Valor inválido. Digite apenas números inteiros.")
        return
    if qtde <= 0:
        print("A quantidade deve ser maior que zero.")
        return

    produto = None
    for p in dados["estoque"]:
        if p["codigoProduto"] == codigo:
            produto = p
            break
    if produto is None:
        print("Produto não encontrado.")
        return

    produto["estoque"] += qtde
    dados["movimentacoes"].append(
        {
            "id": max((m["id"] for m in dados["movimentacoes"]), default=0) + 1,
            "descricao": "Entrada de estoque",
            "codigoProduto": codigo,
            "quantidade": qtde,
        }
    )

    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)

    print(
        f"Entrada registrada. Estoque final de '{produto['descricaoProduto']}': {produto['estoque']}"
    )


def registrar_saida(dados):
    try:
        codigo = int(input("Código do produto: "))
        qtde = int(input("Quantidade de saída: "))
    except ValueError:
        print("Valor inválido. Digite apenas números inteiros.")
        return
    if qtde <= 0:
        print("A quantidade deve ser maior que zero.")
        return

    produto = None
    for p in dados["estoque"]:
        if p["codigoProduto"] == codigo:
            produto = p
            break
    if produto is None:
        print("Produto não encontrado.")
        return
    if produto["estoque"] < qtde:
        print(f"Estoque insuficiente. Disponível: {produto['estoque']}")
        return

    produto["estoque"] -= qtde
    dados["movimentacoes"].append(
        {
            "id": max((m["id"] for m in dados["movimentacoes"]), default=0) + 1,
            "descricao": "Saída de estoque",
            "codigoProduto": codigo,
            "quantidade": qtde,
        }
    )

    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)

    print(
        f"Saída registrada. Estoque final de '{produto['descricaoProduto']}': {produto['estoque']}"
    )


def sair():
    print("Encerrando...")
    sys.exit(0)


def main():
    with open(ARQUIVO, "r", encoding="utf-8") as f:
        dados = json.load(f)

    dados.setdefault("movimentacoes", [])

    while True:
        print("\n=== CONTROLE DE ESTOQUE ===")
        print("1 - Registrar entrada")
        print("2 - Registrar saída")
        print("3 - Sair")
        opcao = input("Escolha: ").strip()

        if opcao == "1":
            registrar_entrada(dados)
        elif opcao == "2":
            registrar_saida(dados)
        elif opcao == "3":
            sair()
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    main()
