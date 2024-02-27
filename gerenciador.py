def escrever_estoque(nome_produto, preco_produto, qtde_produto):
    arquivo = open('lista_de_produtos.txt', 'a')
    arquivo.write(f'{nome_produto} {preco_produto} {qtde_produto} \n')
    arquivo.close()
    
def ler_lista():
    arquivo = open('lista_de_produtos.txt', 'r')
    produtos = arquivo.read()
    arquivo.close()
    return produtos



def mostrar(produtos):
    numero = 1
    for produto in produtos.splitlines():
        print(f'{numero} - {produtos}')
        numero += 1

        
        
def apagar_arquivo():
    arquivo = open('lista_de_produtos.txt', 'a')
    arquivo.write('')
    arquivo.close()