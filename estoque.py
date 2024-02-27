from gerenciador import *

import os

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def pausar():
    input('Digite ENTER para continuar...')

def selecionar_menu(opcao):
    if opcao == '1':
        nome_produto = input("Digite o nome do produto: ")
        preco_produto = input("Digite o preco do produto: ")
        qtde_produto = input("Digite a quantidade do produto: ")
        escrever_estoque(nome_produto, preco_produto, qtde_produto)
    elif opcao == '2':
        produtos = ler_lista()
        mostrar (produtos)
        numero_produto = int(input('Digite o número do produto para atualizar: ')) - 1
        nome_produto = input('Digite o nome do novo produto: ')
        preco_produto = input('Digite o preco do novo produto: ')
        qtde_produto = input('Digite a quantidade do novo produto: ')
        produtos = produtos.splitlines()
        produtos[numero_produto] = nome_produto, preco_produto, qtde_produto
        apagar_arquivo()
        produtos = ' '.join(produtos)
        escrever_estoque(produtos)
        
    elif opcao == '3':
        produtos = ler_lista()
        mostrar(produtos)
        pausar()
    elif opcao == '0':
        print("Obrigada e até mais!")
        exit(0)
        
def exibir_menu():
    limpar_tela()
    print(f"******* MENU *******") 
    print("1 - Adicionar Produto")
    print("2 - Atualizar Produto")
    print("3 - Visualizar Estoque")
    print("0 - Sair do Programa")
    opcao = input("Escolha uma opcão: ")
    selecionar_menu(opcao)
    exibir_menu()
   
exibir_menu()