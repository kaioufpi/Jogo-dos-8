from collections import deque
import no_matriz
from indices import tab
from operator import attrgetter as getatrb

def construir_resposta(no):
	if(no.pai is not None):
		construir_resposta(no.pai)
	print(no.tabuleiro, "Altura: ", no.altura, "\n")


def busca_largura(raiz):
	explorado = deque()
	borda = deque()
	
	borda.append(raiz)
	i = 0
	while borda:
		no_atual = borda.popleft()
		if not(no_atual.tabuleiro in explorado):
			if no_atual.eh_solucao():
				construir_resposta(no_atual)
				print("Posição do nó na fronteira:", i , "Tamanho da borda:", len(borda))
				return
			else:
				novos_filhos = deque(no_atual.gerar_filhos())
				borda.extend(novos_filhos)

			explorado.extend(no_atual.tabuleiro)
		i += 1

def busca_gulosa(raiz):
	explorado = []
	borda = []
	
	i = 0
	borda.append(raiz)
	while borda:
		no_atual = boda.popleft()
		if not(no_atual.tabuleiro in explorado):
			if no_atual.eh_solucao():
				construir_resposta(no_atual)
				print("Posição do nó na fronteira: ", i , "Tamanho da borda: ", len(borda))
				return
			else:
				novos_filhos = no_atual.gerar_filhos()
				borda.extend(novos_filhos)
				borda.sort(key = getatrb("fh"))

			explorado.extend(no_atual.tabuleiro)
		i += 1

raiz = no_matriz.estado([[1, 2, 3], [4, 5, 6], [7, 0, 8]], None, 0, None)
busca_largura(raiz)
