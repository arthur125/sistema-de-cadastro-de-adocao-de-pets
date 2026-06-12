import os

# Declaração das variáveis globais
opcao = 0
usuario = []
animal = []
adocao = []

# Função para limpar a tela
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Função para voltar com enter
def pressione_enter():
    input('Pressione ENTER para continuar...')

# Função para mostrar a logo
def show_title():
    print('''
    ███████╗██╗███████╗████████╗███████╗███╗   ███╗ █████╗     ██████╗ 
    ██╔════╝██║██╔════╝╚══██╔══╝██╔════╝████╗ ████║██╔══██╗    ██╔══██╗
    ███████╗██║███████╗   ██║   █████╗  ██╔████╔██║███████║    ██║  ██║
    ╚════██║██║╚════██║   ██║   ██╔══╝  ██║╚██╔╝██║██╔══██║    ██║  ██║
    ███████║██║███████║   ██║   ███████╗██║ ╚═╝ ██║██║  ██║    ██████╔╝
    ╚══════╝╚═╝╚══════╝   ╚═╝   ╚══════╝╚═╝     ╚═╝╚═╝  ╚═╝    ╚═════╝ 
    ███████╗     █████╗ ██████╗  ██████╗  ██████╗ █████╗  ██████╗      
    ██╔════╝    ██╔══██╗██╔══██╗██╔═══██╗██╔════╝██╔══██╗██╔═══██╗     
    █████╗      ███████║██║  ██║██║   ██║██║     ███████║██║   ██║     
    ██╔══╝      ██╔══██║██║  ██║██║   ██║██║     ██╔══██║██║   ██║     
    ███████╗    ██║  ██║██████╔╝╚██████╔╝╚██████╗██║  ██║╚██████╔╝     
    ╚══════╝    ╚═╝  ╚═╝╚═════╝  ╚═════╝  ╚═════╝╚═╝  ╚═╝ ╚═════╝      
    ██████╗ ███████╗    ██████╗ ███████╗████████╗███████╗              
    ██╔══██╗██╔════╝    ██╔══██╗██╔════╝╚══██╔══╝██╔════╝              
    ██║  ██║█████╗      ██████╔╝█████╗     ██║   ███████╗              
    ██║  ██║██╔══╝      ██╔═══╝ ██╔══╝     ██║   ╚════██║              
    ██████╔╝███████╗    ██║     ███████╗   ██║   ███████║              
    ╚═════╝ ╚══════╝    ╚═╝     ╚══════╝   ╚═╝   ╚══════╝              
                                                    ''')

# Função para exibir os menus
def show_menu(menu, opcoes = True):
    global opcao
    menu_line = '---------------------------'
    clear_screen()
    show_title()

# Menu principal
    if (menu == 'principal'):
        print('1. Usuários')
        print('2. Animais')
        print('3. Adoções')
        print('4. Sair')
# Menu de usuários        
    elif (menu == 'usuario'):
        print('USUÁRIOS')
        print(menu_line)
        print('1. Novo usuário')
        print('2. Ver usuários')
        print('3. Voltar')
    elif (menu == 'novo_usuario'):
        print('NOVO USUÁRIO')
    elif (menu == 'usuario_lista'):
        print('VER USUÁRIOS')
# Menu de animais
    elif (menu == 'animal'):
        print('ANIMAIS')
        print(menu_line)
        print('1. Cadastrar animal')
        print('2. Ver animais')
        print('3. Voltar')
    elif (menu == 'animal_cadastro'):
        print('CADASTAR ANIMAL')
    elif (menu == 'animal_lista'):
        print('VER ANIMAIS')
# Menu de adoções
    elif (menu == 'adocao'):
        print('ADOÇÕES')
        print(menu_line)
        print('1. Adotar animal')
        print('2. Ver animais adotados')
        print('3. Cancelar adoções')
        print('4. Voltar')
    elif (menu == 'animal_adocao'):
        print('ADOTAR ANIMAL')
    elif (menu == 'animal_adotados_lista'):
        print('VER ANIMAIS ADOTADOS')
    elif (menu == 'adocao_cancelamento'):
        print('CANCELAR ADOÇÕES')
    else:
        pass

# Entrada dos menus acima
    print(menu_line)
    if opcoes:
        opcao = input('Escolha a opção desejada: ')

# Sistema de cadastros
def cadastrar(tipo):
# Cadastro de usuários
    if(tipo == 'usuario'):
        codigo = len(usuario) + 1
        nome = input('Digite o nome do usuário: ')
        email = input('Digite o e-mail do usuário: ')
# Se não existir, adicionar usuário a matriz
        usuario.append([codigo, nome, email])
# Cadastro de animais
    elif(tipo == 'animal'):
        codigo = len(animal) + 1
        nome = input('Digite o nome do animal: ')
        idade = float(input('Digite a idade do animal: '))
        raca = input('Digite a raça do animal:')
        porte = input('Digite o porte do animal: ')
# Adicionar animal a matriz
        animal.append([codigo, nome, idade, raca, porte])
# Sistema de adoção
    elif(tipo == 'adocao'):
        numero = len(adocao) + 1
        usuario = int(input('Digite o código do usuário: '))
        animal = int(input('Digite o código do animal: '))
# Adicionar o animal a matriz
        adocao.append([numero, usuario, animal])

# Sistema de listas
def listar(tipo):
    if(tipo == 'usuario'):
        for usuario in usuario:
            print(f'username {usuario[0]} - {usuario[1]} - {usuario[2]}')
    elif(tipo == 'animal'):
        for animal in animal:
            print(f'código {animal[0]} - {animal[1]} - {animal[2]}')