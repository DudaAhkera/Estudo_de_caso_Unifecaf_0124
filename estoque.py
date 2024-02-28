import os



from colorama import init, Fore
init(autoreset=True)

from gerenciador import *



def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')
    
    
def main():
    produtos = []

    while True:
        print(f"{Fore.WHITE}\n -----> Menu <----- :")
        print(f"{Fore.GREEN}1. Adicionar Produtos")
        print(f"{Fore.YELLOW}2. Atualizar Produtos")
        print(f"{Fore.WHITE}3. Visualizar Estoque")
        print(f"{Fore.RED}0. Sair")
        

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
            print(f"{Fore.WHITE}Opção inválida. Digite novamente.")
            
    limpar_tela()

main()