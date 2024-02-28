from colorama import init, Fore
init(autoreset=True)

def escrever_produtos(produto):
    with open("lista_de_produtos.txt", "a") as file:
        file.write(f"{produto}\n")
    
def pausar():
    input(f"{Fore.WHITE}Digite ENTER para continuar...")


def adicionar_produto(produtos):
    nome = input(f"{Fore.GREEN}Digite o nome do produto: ")
    preco = float(input(f"{Fore.GREEN}Digite o preco do produto: "))
    quantidade = int(input(f"{Fore.GREEN}Digite a quantidade do produto: "))
    produto = {"nome": nome, "preço": preco, "quantidade": quantidade}
    produtos.append(produto)
    escrever_produtos(produto)
    print(f"{Fore.GREEN}Produto adicionado!")
    pausar()
def editar_produto(produtos):
    if not produtos:
        print(f"{Fore.YELLOW}Sem produtos disponíveis.")
        return
    
    print(f"{Fore.YELLOW}Lista de produtos:")
    mostrar_produto(produtos)
    
    numero = int(input(f"{Fore.YELLOW}Digite o número do produto a ser atualizado: "))
    
    if 0 <= numero < len(produtos):
        nome = input(f"{Fore.YELLOW}Digite o nome do novo produto: ")
        preco = float(input(f"{Fore.YELLOW}Digite o preço do novo produto: "))
        quantidade = int(input(f"{Fore.YELLOW}Digite a quantidade do novo produto: "))
        
        produtos[numero]["nome"] = nome
        produtos[numero]["preço"] = preco
        produtos[numero]["quantidade"] = quantidade
        
        print(f"{Fore.YELLOW}Produto alterado com sucesso!")
    else:
        print(f"{Fore.YELLOW}Número inválido!")
    pausar()
    
def mostrar_produto(produtos):
    if not produtos:
        print(f"{Fore.LIGHTMAGENTA_EX}Sem produtos disponíveis.")
        
    else:
        print(f"{Fore.LIGHTMAGENTA_EX}Lista de produtos:")
        for numero, produto in enumerate(produtos):
            print(f"{Fore.LIGHTMAGENTA_EX}{numero}. Nome: {produto['nome']} Preço: R${produto['preço']:.2f} Quantidade: {produto['quantidade']} unidade(s)")
