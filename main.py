import datetime

# Dicionário de preços dos refrigerantes
precos = {
    'Fanta Uva': 2.00,
    'Fanta Laranja': 2.50,
    'Sprite': 3.00,
    'Coca Cola': 3.50,
    'Coca Zero': 5.00
}

saldo_usuario = 0.0  # Inicializa o saldo do usuário em zero
# Inicializa a variável para armazenar o refrigerante comprado
refrigerante_comprado = None

# Função para mostrar o menu de refrigerantes e preços


def mostrar_menu():
    print("Menu de Refrigerantes:")
    for refrigerante, preco in precos.items():
        print(f"{refrigerante} - R${preco: .2f}")

# Função para inserir moedas


def inserir_moeda(valor_moeda):
    global saldo_usuario
    saldo_usuario += valor_moeda

# Função para comprar um refrigerante


def comprar_refrigerante(refrigerante):
    global saldo_usuario
    global refrigerante_comprado
    if refrigerante in precos:
        preco_refrigerante = precos[refrigerante]
        if saldo_usuario >= preco_refrigerante:
            saldo_usuario -= preco_refrigerante
            refrigerante_comprado = refrigerante
            data_hora = datetime.datetime.now()
            print(f"Você comprou um {refrigerante} em {data_hora.strftime(
                '%Y-%m-%d %H:%M:%S')}. Seu saldo restante é de R${saldo_usuario: .2f}.")
        else:
            print("Saldo insuficiente. Insira moedas para comprar este refrigerante.")
    else:
        print("Refrigerante não disponível.")


# Loop principal
while True:
    mostrar_menu()
    print(f"Saldo atual: R${saldo_usuario: .2f}")
    opcao = input(
        "Digite 'M' para inserir moedas, ou o nome do refrigerante desejado para comprar: ").strip()

    if opcao == 'M':
        try:
            valor_moeda = float(input("Insira uma moeda (0.25, 0.50, 1.00): "))
            if valor_moeda in [0.25, 0.50, 1.00]:
                inserir_moeda(valor_moeda)
            else:
                print("Moeda não válida.")
        except ValueError:
            print("Valor da moeda inválido.")
    else:
        comprar_refrigerante(opcao)
        if refrigerante_comprado is not None:
            print(f"Você comprou: {refrigerante_comprado}")
