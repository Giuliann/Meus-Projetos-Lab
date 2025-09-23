def menu():
	# Imports dos arquivos:
	from vizualizar import vizu
	from new_user import new_user

	print('Bem-Vindo ao Menu do Banco de Dados\n\n')
	print('(1) Vizualiza o banco de dados')
	print('(2) Adicionar um novo usuario ao banco')
	print('(3) Sair')
	
	select = int(input())
	match select:
		case 1:
			vizu()
		case 2:
			new_user()
		case 3:
			exit()
menu()
