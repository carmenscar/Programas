def usuario_escolhe_jogada(n,m):
	jogada = 0	
	while jogada == 0:
		n = int(input("Quantas peças você vai tirar? "))
		if (n > m) or (n == 0) or (n < 0):
			print("Oops! Jogada inválida! Tente de novo.")
			jogada = 0
		else:
			jogada = 1
	return n
		
def computador_escolhe_jogada(n,m):
	if n <= m:
		return n
	else:
		n = n % (m+1)
		if n > 0:
			return n
		else:
			return m

def campeonato():

	rodada = 1
	while rodada < 4:
		print("\n**** Rodada",rodada," ****\n")
		print(partida())
		rodada += 1
	print("**** Final do campeonato! ****")
	print("Placar: Você 0 X 3 Computador")		

def partida():
	n = int(input("Quantas peças? "))
	m = int(input("Limite de peças por jogada? "))			

	if n % (m + 1) == 0:
		print("\nVocê começa!\n")
		computador = False
	else:
		print("\nComputador começa!\n")
		computador = True

	while n > 0:
		if not computador:
			jogada = usuario_escolhe_jogada(n,m)
			print("Você tirou",jogada,"peças\n")
			computador = True
		else:
			jogada =  computador_escolhe_jogada(n,m)
			print("O computador tirou",jogada,"peças\n")
			computador = False
		
		if (n - jogada) == 1:
			print("Agora resta apenas uma peça no tabuleiro")
		elif (n - jogada) != 0 and (n - jogada) != 0:
			print("Agora restam",n - jogada,"peças no tabuleiro")
		
		n = n-jogada	
	print("Fim do jogo! O computador ganhou!")


def jogo():
	x = int(input("Sua escolha é:"))
	
	if x == 1:
		print("\nVocê escolheu uma partida isolada")
		print(partida())
		print("Placar: Você 0 X 1 Computador")
	elif x == 2:
		print("\nVocê escolheu um campeonato!")
		print(campeonato())
	else:
		print("\nEscolha Inválida\n")
		print(jogo())

print("Bem-vindo ao jogo do NIM! Escolha:\n")
print("1 - para jogar uma partida isolada")
print("2 - para jogar um campeonato ")
print(jogo())	
