'''
Projeto ouvidoria
UNIFACISA
Professor: Daniel Abella
Nome Grupo:
- jose carlos
- klyane cabral
- Felipe Duarte
- Pedro Henrique
- Luis Eduardo

'''

from metodosOuvidoria import *
conexao = abrirBancoDados('localhost','root','root','banco_ouvidoria') #conectando ao banco de dados
ouvidoria = []
opcao = 1


print('Bem-vindo à ouvidoria da Unifacisa🗿🍷')

while opcao != 5:
    print()
    print('Opções: ')
    print('1) Listar ocorrências')
    print('2) Enviar ocorrência')
    print('3) Remover uma ocorrência')
    print('4) Pesquisar uma ocorrência por código')
    print('5) Sair')
    print()
    opcao = int(input('Digite a opção: '))


    if opcao == 1:
        print('Listagem de ocorrências')
        print()
        listaOcorrencia= listarOcorrenciaBD(conexao) #Conectando com o metodo listarOcorrenciaBD

        if len(listaOcorrencia) == 0:
            print('Não existem ocorrências a serem exibidas')
        else:
            for item in listaOcorrencia:
                print('Código', item[0], '|', 'Titulo: ', item[1], '|' , 'Comentario: ', item[2])

    elif opcao == 2:
        print('Adicionar uma nova ocorrência')
        print()
        titulo = input('Digite um titulo: ')
        ocorrencia = input('Digite a Ocorrência: ')

        adicionarOcorrenciaBD(conexao, titulo, ocorrencia) #conectando como metodo adicionarOcorrenciaBD

        print('Ocorrência adicionada com sucesso!')

    elif opcao == 3:
        print('Listagem de ocorrências')
        print()

        listaOcorrencia = listarOcorrenciaBD(conexao) #conectando com o metodo listarOcorrenciaBD

        if len(listaOcorrencia) == 0:
            print('Não existem ocorrências a serem exibidas')
        else:
            for item in listaOcorrencia:
                print('Código', item[0], '|', 'Ocorrência: ', item[1])

        print()

        codigo = input('Digite o código da ocorrência a ser removida: ')


        estaNaLista = estarNaLista(listaOcorrencia,codigo)

        if estaNaLista == True:
            consultaRemoverOcorrencia = 'delete from ouvidoria where codigo = %s '

            dados = (codigo,)

            excluirBancoDados(conexao, consultaRemoverOcorrencia, dados)

            print()
            print('Ocorência removida com sucesso')
        else:
            print('Não há ocorrencia com este código')

    elif opcao == 4:

        print('Pesquisa pelo Código')

        codigo = input('Digite o codigo da ocorrência: ')

        listaOcorrencia = pesquisarOcorrenciaBD(conexao,codigo) #conectando como metodo pesquisarOcorrenciaBD

        if len(listaOcorrencia) == 0:

            print('Não há ocorrência com este código')

        else:
            for item in listaOcorrencia:

                print('Código:', item[0])

                print('Ocorrência:', item[1])

                print()

    elif opcao !=5:
        print('Opção inválida, tente novamente.')

print()
print('A Unifacisa🗿🍷 agradece pelo seu acesso.')
print('Bye!👋')
encerrarBancoDados(conexao) #encerrando a conexão como banco de dados