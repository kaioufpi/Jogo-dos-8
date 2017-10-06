import copy as cp
from indices import tab

class estado(object):
	
	def __init__(self, tabuleiro, pai, altura, movimento):
		self.tabuleiro = tabuleiro
		self.pai = pai
		self.altura = altura
		self.movimento = movimento
		self.fh = self.heuristica()

	def eh_solucao(self):
		if self.tabuleiro == [[1, 2, 3], [4, 5, 6], [7, 8, 0]]:
			return True
		else:
			return False

	def posicao_zero(self):
		for linha in self.tabuleiro:
			try:
				j = linha.index(0)
				break
			except Exception as e: pass
		return self.tabuleiro.index(linha), j

	def posicao_na_matriz(self, valor):
		for i in self.tabuleiro:
			for j in i:
				if j == valor:
					return(self.tabuleiro.index(i), i.index(j))

	def heuristica(self):
		soma = 0

		for i in range(1,9):
			x1, y1 = tab[i]
			x2, y2 = self.posicao_na_matriz(i)

			soma += abs(x1 - x2) + abs(y1-y2)

		return soma


	def filho_esq(self, linha, coluna, filhos):
		aux = self.tabuleiro[linha][coluna - 1]
		novo_tab = cp.deepcopy(self.tabuleiro)
		novo_tab[linha][coluna - 1] = 0
		novo_tab[linha][coluna] = aux
		
		no_filho = estado(novo_tab, self, self.altura + 1, 'esquerda')
		filhos.append(no_filho)

	def filho_dir(self, linha, coluna, filhos):
		aux = self.tabuleiro[linha][coluna + 1]
		novo_tab = cp.deepcopy(self.tabuleiro)
		novo_tab[linha][coluna + 1] = 0
		novo_tab[linha][coluna] = aux

		no_filho = estado(novo_tab, self, self.altura + 1, 'direita')
		filhos.append(no_filho)

	def filho_cima(self, linha, coluna, filhos):
		aux = self.tabuleiro[linha - 1][coluna]
		novo_tab = cp.deepcopy(self.tabuleiro)
		novo_tab[linha - 1][coluna] = 0
		novo_tab[linha][coluna] = aux
		
		no_filho = estado(novo_tab, self, self.altura + 1, 'cima')
		filhos.append(no_filho)

	def filho_baixo(self, linha, coluna, filhos):
		aux = self.tabuleiro[linha + 1][coluna]
		novo_tab = cp.deepcopy(self.tabuleiro)
		novo_tab[linha + 1][coluna] = 0
		novo_tab[linha][coluna] = aux
		
		no_filho = estado(novo_tab, self, self.altura + 1, 'baixo')
		filhos.append(no_filho)

	def gerar_filhos(self):
		linha,coluna = self.posicao_zero()
		filhos = []

		if coluna <= 1:
			self.filho_dir(linha, coluna, filhos)
			if coluna == 1:
				self.filho_esq(linha, coluna, filhos)
		else:
			self.filho_esq(linha, coluna, filhos)
		
		if linha <= 1:
			self.filho_baixo(linha, coluna, filhos)
			if linha == 1:
				self.filho_cima(linha, coluna, filhos)
		else:
			self.filho_cima(linha, coluna, filhos)

		return filhos
