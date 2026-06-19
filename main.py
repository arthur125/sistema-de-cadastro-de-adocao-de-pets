import os

# Declaração das variáveis globais
opcao = 0
usuarios = []
animais = []
adocoes = []

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
        print('USUÁRIO')
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
        print('ANIMAL')
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
    if(tipo == 'usuarios'):
        codigo = len(usuarios) + 1
        nome = input('Digite o nome do usuário: ')
        email = input('Digite o e-mail do usuário: ')
# Se não existir, adicionar usuário a matriz
        usuarios.append([codigo, nome, email])
# Cadastro de animais
    elif(tipo == 'animais'):
        codigo = len(animais) + 1
        nome = input('Digite o nome do animal: ')
        idade = float(input('Digite a idade do animal: '))
        raca = input('Digite a raça do animal:')
        porte = input('Digite o porte do animal: ')
# Adicionar animal a matriz
        animais.append([codigo, nome, idade, raca, porte])
# Sistema de adoção
    elif(tipo == 'adocoes'):
        numero = len(adocoes) + 1
        usuario = int(input('Digite o código do usuário: '))
        animal = int(input('Digite o código do animal: '))
# Adicionar o animal a matriz
        adocoes.append([numero, usuarios, animais])

# Sistema de listas
def listar(tipo):
    if(tipo == 'usuarios'):
        for usuario in usuarios:
            print(f'username {usuario[0]} - {usuario[1]} - {usuario[2]}')
    elif(tipo == 'animais'):
        for animal in animais:
            print(f'código {animal[0]} - {animal[1]} - {animal[2]}')
    elif(tipo == 'adocoes'):
        for adocao in adocoes:
            print(f'adocao {adocao[0]} - usuário {usuarios[adocao[1]-1][1]} - animal {animais[adocao[2]-1][1]} - adocao = {adocoes[3]}')
    else:
        print('Não há valores a exibir...')
        pressione_enter()

while True:
    show_menu('principal')

    if(opcao == '1'):
        show_menu('usuario')
        if(opcao == '1'):
            show_menu('novo_usuario', False)
            cadastrar('usuarios') 
        elif(opcao == '2'):
            show_menu('usuario_lista', False)
            listar('usuarios')
            pressione_enter()
        elif(opcao == '4'):
            print('VOLTAR')
        else:
            print('Opção inválida...')
    elif(opcao == '2'):
        show_menu('animal')
        if(opcao == '1'):
            show_menu('animal_cadastro', False)
            cadastrar('animais') 
        elif(opcao == '2'):
            show_menu('animal_lista', False)
            listar('animais')
            pressione_enter()
        elif(opcao == '4'):
            print('VOLTAR')
        else:
            print('Opção inválida...')
    elif(opcao == '3'):
        show_menu('adocao')
        if(opcao == '1'):
            show_menu('animal_adocao', False)
            cadastrar('adocoes') 
        elif(opcao == '2'):
            show_menu('animal_adotados_lista', False)
            listar('adocoes')
            pressione_enter()
        elif(opcao == '4'):
            print('VOLTAR')
        else:
            print('Opção inválida...')
    elif(opcao == '4'):
        break
    else:
        print('Opção inválida! Digite uma opção do menu...')

clear_screen()
print('O programa foi encerrado.')