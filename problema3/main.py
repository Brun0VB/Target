from datetime import date, datetime

TAXA_DIARIA = 0.025

def jurosComposto(dias,valor):
    juros = valor * ((1+TAXA_DIARIA)**dias - 1)
    return juros   

def jurosSimples(dias,valor):
    juros = valor * TAXA_DIARIA * dias
    return juros

def main():
    try:
        valor = float(input("Valor (ex: 1500.00): "))
        vencimento = datetime.strptime(
            input("Data de vencimento (dd/mm/aaaa): ").strip(), "%d/%m/%Y"
        ).date()
        print("\nTipo de juros:")
        print("1 - Simples")
        print("2 - Composto")
        tipo = input("Escolha: ").strip()
    except ValueError:
        print("Entrada inválida. Use números no valor e a data no formato dd/mm/aaaa.")
        return

    if valor <= 0:
        print("O valor deve ser maior que zero.")
        return

    if tipo != "1" and tipo != "2":
        print("Escolha de juros inválida.")
        return

    hoje = date.today()
    dias_atraso = (hoje - vencimento).days

    if dias_atraso <= 0:
        print("Não há atraso. Juros: R$ 0,00")
        return

    if tipo == "1":
        juros = jurosSimples(dias_atraso,valor)
    else:
        juros = jurosComposto(dias_atraso,valor)

    total = valor + juros

    print(f"\nDias de atraso: {dias_atraso}")
    print(f"Juros: R$ {juros:,.2f}")
    print(f"Total a pagar: R$ {total:,.2f}")


if __name__ == "__main__":
    main()