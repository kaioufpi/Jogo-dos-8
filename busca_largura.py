from collections import deque
import no_matriz

def busca_largura(raiz):


	explorado = deque()
	borda.append(raiz)
	i = 0
	while borda:
		if not(borda[i].tabuleiro in explorado):
			if borda[i].eh_solucao():
				print(borda[i].tabuleiro)
				input('Resposta acima')
				return
			else:
				print(borda[i].tabuleiro)
				input('Não é a resposta')

				novos_filhos = borda[i].gerar_filhos()
				borda.extend(novos_filhos)

			explorado.extend(borda[i].tabuleiro)
		i += 1

borda = deque()

raiz = no_matriz.estado([[1, 2, 3], [4, 5, 6], [0, 7, 8]], None, 0)
busca_largura(raiz)


