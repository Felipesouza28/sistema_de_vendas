estoque_produtos = {
    1: {"nome": "Monitor Gamer LG UltraGear™ Curvo 34P", "preco": 2049.00, "quantidade": 20},
    2: {"nome": "Teclado Gamer Magnético Akko Monsgeek Fun60 Pro", "preco": 263.84, "quantidade": 80},
    3: {"nome": "Cpu Pc Gamer Intel Core I5 3.6ghz Ram 16gb Ssd 500gb", "preco": 2100.00, "quantidade": 30},
    4: {"nome": "Headphone Fone de Ouvido H2002d Gamer", "preco": 150.00, "quantidade": 60},
    5: {"nome": "SSD SATA A400, Kingston 240G", "preco": 360.00, "quantidade": 25},
    6: {"nome": "SSD Kingston NV3 1TB M.2 2280 NVMe", "preco": 849.90, "quantidade": 15}
}

carrinho = []

import time
while True:

    print("-"*20)
    print("Bem vindo TecGames!🤖")
    print("-"*20)
    time.sleep(0.8)
    print("[1] Visualizar Estoque")
    print("[2] Adicionar Item ao Carrinho")
    print("[3] Visualizar Carrinho")
    print("[4] Finalizar Compra")
    print("[0] Sair do Sistema")

    opcao = int(input("\nEscolha uma opção: \n"))
    if opcao == 1:
        print("Visualizando estoque!")
        print("ID |                 Nome                |   Valor   | Quantidade")
        for k,v in estoque_produtos.items():
            print(f"{k} | {v["nome"]} | {v["preco"]} | {v["quantidade"]} ")

    elif opcao == 2:
        print("Adicionando itens ao carrinho!")
        for k,v in estoque_produtos.items():
            print(f"{k} | {v["nome"]} | {v["preco"]} | {v["quantidade"]} ")
            id_produto = int(input("Qual o id do produto que deseja comprar? "))
            if id_produto in estoque_produtos:
                qtd_produto = int(input("Quantas unidades voce deseja?"))
                if qtd_produto <=0:
                    print("Quantidade inválida")
                elif qtd_produto <= estoque_produtos[id_produto]["quantidade"]:
                    carrinho.append(estoque_produtos[id_produto])
                    estoque_produtos[id_produto]["quantidade"] -= qtd_produto

    elif opcao == 3:
        print("Visualizando carrinho!")

    elif opcao == 4:
        print("Finalizando compras!")

    elif opcao == 0:
        print("Saindo do Site")
        break

    else:
        print("Esse número não é válido!\nDigite um número que esteja no menu!")




