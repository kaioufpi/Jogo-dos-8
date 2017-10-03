from collections import deque
import no_matriz

def construir_resposta(no):
	if(no.pai is not None):
		construir_resposta(no.pai)
	print(no.tabuleiro, "Altura: ", no.altura, "\n")


def busca_largura(raiz):
	explorado = deque()
	borda.append(raiz)
	i = 0
	while borda:
		no_atual = borda.popleft()
		if not(no_atual in explorado):
			if no_atual.eh_solucao():
				construir_resposta(no_atual)
				'''
				print("Pai: ", borda[i].pai, "Explorado: ", borda[i].tabuleiro, borda[i].movimento, "Altura: ", borda[i].altura)
				print('Resposta acima\n')
				'''
				print("Posição do nó na fronteira: ", i , "Tamanho da borda: ", len(borda))
				return
			else:
				novos_filhos = no_atual.gerar_filhos()
				borda.extend(novos_filhos)

			explorado.extend(no_atual.tabuleiro)
		i += 1


borda = deque()
raiz = no_matriz.estado([[1, 2, 3], [0, 4, 5], [7, 8, 6]], None, 0, None)
busca_largura(raiz)


