# coding=utf-8
# Programa Nanodegree Introdução à Programação - Udacity
# Projeto - Programe seu Próprio Quiz
# Autor: Leandro Inacio

# perguntas do quiz
frase_nivel_facil = """Python eh uma linguagem de __0__ de alto nivel. Html eh uma
linguagem de __1__ de __2__. E o CSS eh uma linguagem de folha de __3__ ."""

frase_nivel_medio = """No Python a função __0__ eh utilizada para imprimir os
argumentos passados a ela no __1__ . Em Html a tag __2__ eh utilizada para
especificar um titulo para o documento Html. Os __3__ no CSS sao usados ​​para
"localizar" (ou selecionar) elementos HTML com base no nome, ID, classe,
atributo e mais do elemento."""

frase_nivel_dificil = """Em Python, definimos uma funcao, tambem chamado de
procedimento, utilizando a palavra reservada __0__ . No Html utilizamos a
tag __1__ para inserir uma imagem e utlizamos o atributo __2__ para fornecer um
texto alternativo para uma imagem. No CSS, utilizamos a propriedade __3__ para
especificar a cor do texto."""

# repostas do quiz
resposta_nivel_facil = ['programacao', 'marcacao', 'hipertexto', 'estilos']
resposta_nivel_medio = ['print', 'terminal', 'title', 'seletores']
resposta_nivel_dificil = ['def', 'img', 'alt', 'color']

# listas principais
_chances = [3, 2, 1]
_niveis_de_dificuldade = ['facil', 'medio', 'dificil']
_frases = [frase_nivel_facil, frase_nivel_medio, frase_nivel_dificil]
_espacos = ['__0__','__1__','__2__','__3__']
_respostas = [resposta_nivel_facil, resposta_nivel_medio, resposta_nivel_dificil]

def msg_inicial():
    # mostra uma mensagem inicial do programa
     print '\n\n -------------------------------------------------'
     print '|     Bem vindo ao Quiz de Python, Html e CSS     |'
     print ' -------------------------------------------------\n'

def captura_nome():
    # captura o nome do usuario e dá uma msg de boas vindas
    usuario = raw_input("\nPor favor, informe o seu nome: ")
    print "\nBem vido " + usuario + '!!\n\n'
    return usuario

def escolha_de_nivel():
    # Essa função define o nível do jogo escolhido pelo usuario.
    while True:
        nivel = raw_input('Escolha o nivel do jogo: facil | medio | dificil: ').lower()
        if nivel in _niveis_de_dificuldade:
            print '\nOk, voce escolheu o nivel: ' + nivel + '.\n'
            return nivel
        print 'Escolha errada! Tente novamente.\n'

def controlar_nivel():
    # Essa função controla e envia para o jogo a frase e a lista de respostas,
    # de acordo com o nível escolhido.
    nivel           = escolha_de_nivel()
    indice_do_nivel = _niveis_de_dificuldade.index(nivel)

    jogar_nivel(_frases[indice_do_nivel], _respostas[indice_do_nivel], _chances[indice_do_nivel])

def jogar_nivel(frase, respostas, num_chances):
    # Esse método processa o nível escolhido e manipula a frase e as respostas desse nível.
    print ("\nDe acordo com o nivel escolhido, voce tem {} chances de errar!\n\n".format(num_chances))
    indice = 0
    while num_chances >= 0 and indice < len(respostas):
        print frase
        resposta = raw_input("\nA palavra do campo {} eh? ".format(_espacos[indice]).lower())
        if resposta == respostas[indice]:
            frase = frase.replace('__' + str(indice) + '__', resposta)
            print "\nAcertou!!\n"
            indice += 1
            if indice == len(respostas):
                print frase
        else:
            num_chances -= 1
            print "\nResposta errada. Voce tem mais " + str(num_chances) + " tentativa(s).\n"


def mensagem_final():
    # função que mostra uma mensagem Final
    print '\nMuito obrigado e ate a proxima!'

def main():
    # função utilizada para invocar todas as outras funções do programa.
    msg_inicial()
    captura_nome()
    controlar_nivel()
    mensagem_final()

# inicia o programa
main()
