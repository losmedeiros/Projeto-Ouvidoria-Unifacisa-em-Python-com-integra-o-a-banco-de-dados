from operacoesbd import *

def listarOcorrenciaBD(conexao):
    consultaListagemOcorrencia = 'select * from ouvidoria'

    listaOcorrencia = listarBancoDados(conexao, consultaListagemOcorrencia)

    return listaOcorrencia

def adicionarOcorrenciaBD(conexao,titulo,ocorrencia):
    consultaNovaOcorrencia = 'insert into ouvidoria (titulo, comentario) values(%s, %s)'

    dados = (titulo,ocorrencia)

    insertNoBancoDados(conexao, consultaNovaOcorrencia, dados)

def removerOcorrenciaBD(conexao,codigo):
    consultaRemoverOcorrencia = 'delete from ouvidoria where codigo = %s '

    dados = (codigo)

    excluirBancoDados(conexao, consultaRemoverOcorrencia,dados)

def pesquisarOcorrenciaBD(conexao,codigo):
    consultaOcorrenciaPorCodigo = 'select * from ouvidoria where codigo = ' + codigo

    listaOcorrencia = listarBancoDados(conexao, consultaOcorrenciaPorCodigo)

    return listaOcorrencia

def estarNaLista(listaOcorrencia,codigo):
    estaNaLista = False

    for item in listaOcorrencia:
        if item[0] == int(codigo):

            estaNaLista = True

            break

        else:

            estaNaLista = False

    return estaNaLista