def menu():
	# Imports dos arquivos:
	from vizualizar import vizu
	from new_user import new_user
	from delete_user import delete

	print('Bem-Vindo ao Menu do Banco de Dados\n\n')
	print('(1) Vizualiza o banco de dados')
	print('(2) Adicionar um novo usuario ao banco')
	print('(3) Remove um usuario do banco')
	print('(4) Sair')
	
	select = int(input())
	match select:
		case 1:
			vizu()
		case 2:
			new_user()
		case 3:
			delete()
		case 4:
			exit()
menu()
