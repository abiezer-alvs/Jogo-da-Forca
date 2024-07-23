print()
print("Bem vindo ao jogo da forca! Bora jogar?!")
print()
nome_do_jogador = input("Qual o seu nome? ")
print()
print("{}, escolha um tema para o jogo de acordo com o número:\nAnimes(0), Time de futebol(1), Jogos pc(2), Países(3) ou Matérias escolares(4) ".format(nome_do_jogador))  
print()
tema_da_forca = int(input("Tema: "))
def Forca():
	animes = ["One-piece", "Dragon-Ball", "Naruto", "Shingeki-no-Kyojin", "Kimetsu-no-Yaiba", "Shigatsu-wa-Kimi-no-Uso", "Tokyo-Ghoul"]
	times_de_futebol = ["Gremio", "Internacional", "Flamengo", "Palmeiras", "Sao-Paulo", "Fluminense", "Vasco"]
	jogos_de_pc = ["Genshin-Impact", "Valorant", "League-of-Legends", "Call-of-Duty", "It-Takes-Two", "Playerunknowsbatllegrounds", "Dota"]
	paises = ["Brasil", "Estados-Unidos", "Alemanha", "Dinamarca", "Espanha", "Argentina", "Chile"]
	materias = ["Geografia", "Matematica", "Sociologia", "Biologia", "Historia", "Portugues", "Filosofia"]
	temas_gerais = [animes, times_de_futebol, jogos_de_pc, paises, materias]
	temas_escolhido = ["Animes", "Time de futebol", "Jogos de PC", "Países", "Materias escolares"]
	import random
	palavra_escolhida = random.choice(temas_gerais[tema_da_forca]).upper()
	chances = 6
	alfabeto = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ-")
	tentativas_de_letra = []
	erros = 0
	print("O tema é: {}".format(temas_escolhido[tema_da_forca]))
	while True:
		print()
		print(tentativas_de_letra)
		print()
		print("Chances: ",chances)
		print()
		for letra in palavra_escolhida:
			if letra in tentativas_de_letra:
				print(letra, end = ' ')
			else:
				print('_', end= ' ')
		print()
		palpite = input("\nDigite uma letra: ").upper()
		print()
		if palpite not in alfabeto or palpite == '':
			print("Desculpe, mas isso não está na palavra")
			print()
			continue	
		elif palpite in tentativas_de_letra:
			print("Você ja tentou essa letra!")
			print()
			continue
		tentativas_de_letra.append(palpite)
		if palpite in palavra_escolhida:
			print("Boa {} você acertou uma das letras, continue assim!".format(nome_do_jogador))
			print()
		else:
			chances -= 1
			print("Errou, tenta denovo")
			erros += 1
			print()
		if erros == 0:
			print("  ____________")
			print(" |       |    ")
			print(" |       |    ")
			print(" |            ")
			print(" |            ")
			print(" |            ")
			print(" |            ")
		elif erros == 1:
				print("  ____________")
				print(" |       |    ")
				print(" |       |    ")
				print(" |     ('-')  ")
				print(" |            ")
				print(" |            ")
				print(" |            ")
		elif erros == 2:
				print("  ____________")
				print(" |       |    ")
				print(" |       |    ")
				print(" |     ('-')  ")
				print(" |      \     ")
				print(" |            ")
				print(" |            ")	
		elif erros == 3:
				print("  ____________")
				print(" |       |    ")
				print(" |       |    ")
				print(" |     ('-')  ")
				print(" |      \|    ")
				print(" |       |    ")
				print(" |            ")
		elif erros == 4:
				print("  ____________")
				print(" |       |    ")
				print(" |       |    ")
				print(" |     ('-')  ")
				print(" |      \|/   ")
				print(" |       |    ")
				print(" |            ")
		elif erros == 5:
				print("  ____________")
				print(" |       |    ")
				print(" |       |    ")
				print(" |     ('-')  ")
				print(" |      \|/   ")
				print(" |       |    ")
				print(" |      /     ")
		elif erros == 6:
				print("  ____________")
				print(" |       |    ")
				print(" |       |    ")
				print(" |     ('-')  ")
				print(" |      \|/   ")
				print(" |       |    ")
				print(" |      / \   ")
		if chances == 0:
			print()
			print("{}, infelizmente você perdeu\nA palavra era {}".format(nome_do_jogador, palavra_escolhida))
			print("    _______________         ")
			print("   /               \       ")
			print("  /                 \      ")
			print("//                   \/\  ")
			print("\|   XXXX     XXXX   | /   ")
			print(" |   XXXX     XXXX   |/     ")
			print(" |   XXX       XXX   |      ")
			print(" |                   |      ")
			print(" \__      XXX      __/     ")
			print("   |\     XXX     /|       ")
			print("   | |           | |        ")
			print("   | I I I I I I I |        ")
			print("   |  I I I I I I  |        ")
			print("   \_             _/       ")
			print("     \_         _/         ")
			print("       \_______/           ")
			break
		elif set(palavra_escolhida).issubset(set(tentativas_de_letra)):
					print()
					print("Parabéns {}, você acertou todas as letras".format(nome_do_jogador))
					print("A palavra era {}".format(palavra_escolhida))
					print("       ___________      ")
					print("      '._==_==_=_.'     ")
					print("      .-\\:      /-.    ")
					print("     | (|:.     |) |    ")
					print("      '-|:.     |-'     ")
					print("        \\::.    /      ")
					print("         '::. .'        ")
					print("           ) (          ")
					print("         _.' '._        ")
					print("        '-------'       ")
					break
Forca()
while True:
	jogar_denovo = input("{}, você deseja jogar novamente? ".format(nome_do_jogador)).lower()
	if jogar_denovo == "sim":
		Forca()
	else:
		print("{}, muito obrigado! será sempre bem vindo novamente".format(nome_do_jogador))
		break
