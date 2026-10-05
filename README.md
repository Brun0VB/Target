# Desafio Target

## Visão geral

O projeto foi organizado em três pastas independentes:

- `problema1/`: cálculo de comissão por vendedor;
- `problema2/`: controle de estoque com entrada e saída de produtos;
- `problema3/`: cálculo de juros por atraso em uma cobrança.

Como não houve especificação de linguagem, as implementações foram realizadas em python.

## Estrutura do projeto

```text
DesafioTarget/
├── problema1/
│   ├── data.json
│   └── main.py
├── problema2/
│   ├── data.json
│   └── main.py
├── problema3/
│   └── main.py
├── .gitignore
├── .python-version
├── pyproject.toml
├── uv.lock
├── README.md
└── .venv/
```

## Requisitos

- Python 3.10 ou superior
- (Opcional) `uv` para gerenciamento do ambiente

## Como executar

A partir da raiz do projeto, execute os scripts diretamente:

```bash
python problema1/main.py
python problema2/main.py
python problema3/main.py
```

Se preferir usar `uv`:

```bash
uv run python problema1/main.py
uv run python problema2/main.py
uv run python problema3/main.py
```

## Descrição dos desafios

### Problema 1: comissão por vendedor

A pasta `problema1/` contém um script que lê os dados de vendas de um arquivo JSON e calcula a comissão de cada vendedor conforme as regras:

- valores menores que 100: comissão de 0%
- valores entre 100 e 499,99: comissão de 1%
- valores iguais ou acima de 500: comissão de 5%

O resultado é exibido por vendedor com o total acumulado.

### Problema 2: controle de estoque

A pasta `problema2/` implementa um menu interativo para:

- registrar entrada de produtos;
- registrar saída de produtos;
- validar quantidade disponível em estoque;
- persistir as movimentações no arquivo `data.json`.

O sistema trabalha com uma base de produtos e atualiza o estoque em memória e no arquivo JSON.

### Problema 3: juros por atraso

A pasta `problema3/` contém um programa que solicita:

- valor da dívida;
- data de vencimento;
- tipo de juros: simples ou composto.

A taxa diária aplicada é de 2,5% e o valor total é calculado de acordo com os dias de atraso.

## Observações

- Os dados de entrada dos desafios ficam em arquivos JSON dentro de cada pasta.

- Não há dependências externas além do Python padrão.


