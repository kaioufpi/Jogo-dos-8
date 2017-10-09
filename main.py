from collections import deque
import no_matriz
from indices import tab
from operator import attrgetter as getatrb
from time import time
from movimentos import qtMov
def construir_resposta(no):
    if(no.pai is not None):
        construir_resposta(no.pai)
    print(no.tabuleiro, "Altura: ", no.altura, "\n", ", Heuristica: ", no.fh, ", A*: ", no.a_estrela())


def busca_largura(raiz):
    explorado = []
    borda = deque()
    
    borda.append(raiz)
    i = 0
    while borda:
        no_atual = borda.popleft()
        if not(no_atual.tabuleiro in explorado):
            if no_atual.eh_solucao():
                construir_resposta(no_atual)
                print("Posição do nó na fronteira: ", i , "Tamanho da borda: ", len(borda), "Altura: ", no_atual.altura)
                return
            else:
                novos_filhos = no_atual.gerar_filhos()
                borda.extend(novos_filhos)

            explorado.extend(no_atual.tabuleiro)
        i += 1

def busca_profundidade(raiz):

    borda = deque()
    ultimos = deque()
    tamanho__da_memoria = 3
    borda.append(raiz)
    i = 0

    for i in range(tamanho__da_memoria):
        no_atual = borda.popleft()
        if not(no_atual.tabuleiro in ultimos):
            if no_atual.eh_solucao():
                construir_resposta(no_atual)
                print("Posição do nó na fronteira: ", i , "Tamanho da borda: ", len(borda), "Altura: ", no_atual.altura)
                return
            else:
                novos_filhos = no_atual.gerar_filhos()
                borda.extend(novos_filhos)

            ultimos.append(no_atual.tabuleiro)
        i += 1

    while borda:
        no_atual = borda.popleft()
        if not(no_atual.tabuleiro in ultimos):
            if no_atual.eh_solucao():
                #construir_resposta(no_atual)
                print("Posição do nó na fronteira: ", i , "Tamanho da borda: ", len(borda), "Altura: ", no_atual.altura)
                return
            else:
                novos_filhos = no_atual.gerar_filhos()
                borda.extend(novos_filhos)

            ultimos.popleft()
            ultimos.append(no_atual.tabuleiro)
        i += 1

def busca_heuristica(raiz):
    explorado = []
    borda = []
    
    i = 0
    borda.append(raiz)
    while borda:
        no_atual = borda.pop(0)
        if not(no_atual.tabuleiro in explorado):
            if no_atual.eh_solucao():
                construir_resposta(no_atual)
                print("Posição do nó na fronteira: ", i , "Tamanho da borda: ", len(borda), "Altura: ", no_atual.altura)
                return
            else:
                novos_filhos = no_atual.gerar_filhos()
                borda.extend(novos_filhos)
                borda.sort(key = lambda a : a.a_estrela())

            explorado.extend(no_atual.tabuleiro)
        i += 1

def busca_gulosa(raiz):
    explorado = []
    borda = []
    
    i = 0
    borda.append(raiz)
    while borda:
        no_atual = borda.pop(0)
        if not(no_atual.tabuleiro in explorado):
            if no_atual.eh_solucao():
                construir_resposta(no_atual)
                print("Posição do nó na fronteira: ", i , "Tamanho da borda: ", len(borda), "Altura: ", no_atual.altura)
                return
            else:
                novos_filhos = no_atual.gerar_filhos()
                borda.extend(novos_filhos)
                borda.sort(key = getatrb('fh'))

            explorado.extend(no_atual.tabuleiro)
        i += 1
    
def run(vetor, alg):
    raiz = no_matriz.estado(vetor, None, 0, None)

    if(alg=='1'):
        inicio = time()
        busca_largura(raiz)
        fim = time()
        print("\n\nLargura: ", fim - inicio, "\n\n")
    if(alg=='2'):
        inicio = time()
        busca_profundidade(raiz)
        fim = time()
        print("\n\nProfundidade: ", fim - inicio, "\n\n")
    if(alg=='3'):
        inicio = time()
        busca_heuristica(raiz)
        fim = time()
        print("\n\nHeuristica: ", fim - inicio, "\n\n")
    if(alg=='4'):
        inicio = time()
        busca_gulosa(raiz)
        fim = time()
        print("\n\nGulosa: ", fim - inicio, "\n\n")

