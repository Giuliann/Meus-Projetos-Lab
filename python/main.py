def menu():
	# Imports dos arquivos:
	from vizualizar import vizu

	print('Bem-Vindo ao Menu do Banco de Dados\n\n')
	print('(1) Vizualiza o banco de dados')
	print('(2) Sair')
	
	select = int(input())
	match select:
		case 1:
			vizu()
		case 2:
			exit()
menu()
