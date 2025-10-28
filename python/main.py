def menu():
	# Importando a Classe: 
	from banco import Banco

	# Chamando classe e nomeando os objetos: 
	Dos_Csv = Banco(nome='Dos_Csv')
	Intrusion_Csv = Banco(nome='Intrusion_Csv')
	MitM_Csv = Banco(nome='MitM_Csv')

	# Menu
	print('\n\nBem-Vindo ao Menu do Banco de Dados\n\n')
	print('(1) Acessar banco de dados Dos_Csv')
	print('(2) Aecssar banco de dados Instrsion_Csv')
	print('(3) Acessar banco de dados Mitm_Csv')
	print('(4) Encerrar programa')

	# Seleção das opções do menu: 
	select = int(input())	
	match select:
		case 1:
			# Dados do Banco Dos_Csv.db: 
			Dos_Csv.nome_tabela()
			Dos_Csv.conexao()
			Dos_Csv.nome_coluna()
			Dos_Csv.array_numpy()
			input('Pressione Enter para continuar com a vizualização das Arrays...')
			Dos_Csv.exibir()
			input('Pressione Enter para continuar com a vizualização das Ocorrencias...')
			Dos_Csv.ocorrencias()
			print('\n\nDeseja voltar para o menu?')

			# Voltar para o menu: 
			print('(1) Sim')
			print('(2) Não')
			select = int(input(''))
			match select:
				case 1:
					menu()
				case 2:
					exit('Promgrama encerrado...')
		case 2:
			# Dados do Banco Instrusio_Csv.db: 
			Intrusion_Csv.nome_tabela()
			Intrusion_Csv.conexao()
			Intrusion_Csv.nome_coluna()
			Intrusion_Csv.array_numpy()
			input('Pressione Enter para continuar com a vizualização das Arrays...')
			Intrusion_Csv.exibir()
			input('Pressione Enter para continuar com a vizualização das Ocorrencias...')
			Intrusion_Csv.ocorrencias()
			print('\n\nDeseja voltar para o menu?')

			# Voltar para o menu: 
			print('(1) Sim')
			print('(2) Não')
			select = int(input(''))
			match select:
				case 1:
					menu()
				case 2:
					exit('Promgrama encerrado...')
		case 3:
			# Dados do Banco MitM_Csv.db: 
			MitM_Csv.nome_tabela()
			MitM_Csv.conexao()
			MitM_Csv.nome_coluna()
			MitM_Csv.array_numpy()
			input('Pressione Enter para continuar com a vizualização das Arrays...')
			MitM_Csv.exibir()
			input('Pressione Enter para continuar com a vizualização das Ocorrencias...')
			MitM_Csv.ocorrencias()
			print('\n\nDeseja voltar para o menu?')

			# Voltar para o menu: 
			print('(1) Sim')
			print('(2) Não')
			select = int(input(''))
			match select:
				case 1:
					menu()
				case 2:
					exit('Promgrama encerrado...')
		case 4:
			exit('Programa encerrado...') 
	
menu()
