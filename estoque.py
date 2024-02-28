import os

from colorama import init, Fore
init(autoreset=True)

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def pausar():
    input("Digite ENTER para continuar...")


def adicionar_produto(produtos):
    nome = input("Digite o nome do produto: ")
    preco = float(input("Digite o preco do produto: "))
    quantidade = int(input("Digite a quantidade do produto: "))
    produto = {"nome": nome, "preço": preco, "quantidade": quantidade}
    produtos.append(produto)
    print("Produto adicionado!")
    pausar()
def editar_produto(produtos):
    if not produtos:
        print("Sem produtos disponíveis.")
        return
    
    print("Lista de produtos:")
    mostrar_produto(produtos)
    
    numero = int(input("Digite o número do produto a ser atualizado: "))
    
    if 0 <= numero < len(produtos):
        nome = input("Digite o nome do novo produto: ")
        preco = float(input("Digite o preço do novo produto: "))
        quantidade = int(input("Digite a quantidade do novo produto: "))
        
        produtos[numero]["nome"] = nome
        produtos[numero]["preço"] = preco
        produtos[numero]["quantidade"] = quantidade
        
        print("Produto alterado com sucesso!")
    else:
        print("Número inválido!")
    pausar()
def mostrar_produto(produtos):
    if not produtos:
        print("Sem produtos disponíveis.")
    else:
        print("Lista de produtos:")
        for numero, produto in enumerate(produtos):
            print(f"{numero}. Nome: {produto['nome']} Preço: {produto['preço']} Quantidade: {produto['quantidade']}")

def main():
    produtos = []

    while True:
        print("\nMenu:")
        print("1. Adicionar Produtos")
        print("2. Atualizar Produtos")
        print("3. Visualizar Estoque")
        print("0. Sair")
        

        opcao = input("Digite a opção desejada: ")

        if opcao == "1":
            adicionar_produto(produtos)
        elif opcao == "2":
            editar_produto(produtos)
        elif opcao == "3":
            mostrar_produto(produtos)
        elif opcao == "0":
            break
        else:
            print("Opção inválida. Digite novamente.")
            
    limpar_tela()

main()