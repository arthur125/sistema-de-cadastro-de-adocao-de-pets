import os

# Declaração das variáveis globais
opcao = 0
clientes = []
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
    ███████╗██╗███████╗████████╗███████╗███╗   ███╗ █████╗     ██████╗ ███████╗                                
    ██╔════╝██║██╔════╝╚══██╔══╝██╔════╝████╗ ████║██╔══██╗    ██╔══██╗██╔════╝                                
    ███████╗██║███████╗   ██║   █████╗  ██╔████╔██║███████║    ██║  ██║█████╗                                  
    ╚════██║██║╚════██║   ██║   ██╔══╝  ██║╚██╔╝██║██╔══██║    ██║  ██║██╔══╝                                  
    ███████║██║███████║   ██║   ███████╗██║ ╚═╝ ██║██║  ██║    ██████╔╝███████╗                                
    ╚══════╝╚═╝╚══════╝   ╚═╝   ╚══════╝╚═╝     ╚═╝╚═╝  ╚═╝    ╚═════╝ ╚══════╝                                
     ██████╗ █████╗ ██████╗  █████╗ ███████╗████████╗██████╗  ██████╗     ██████╗ ███████╗                     
    ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔════╝╚══██╔══╝██╔══██╗██╔═══██╗    ██╔══██╗██╔════╝                     
    ██║     ███████║██║  ██║███████║███████╗   ██║   ██████╔╝██║   ██║    ██║  ██║█████╗                       
    ██║     ██╔══██║██║  ██║██╔══██║╚════██║   ██║   ██╔══██╗██║   ██║    ██║  ██║██╔══╝                       
    ╚██████╗██║  ██║██████╔╝██║  ██║███████║   ██║   ██║  ██║╚██████╔╝    ██████╔╝███████╗                     
    ╚═════╝╚═╝  ╚═╝╚═════╝ ╚═╝  ╚═╝╚══════╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝     ╚═════╝ ╚══════╝                     
     █████╗ ██████╗  ██████╗  ██████╗ █████╗  ██████╗     ██████╗ ███████╗    ██████╗ ███████╗████████╗███████╗
    ██╔══██╗██╔══██╗██╔═══██╗██╔════╝██╔══██╗██╔═══██╗    ██╔══██╗██╔════╝    ██╔══██╗██╔════╝╚══██╔══╝██╔════╝
    ███████║██║  ██║██║   ██║██║     ███████║██║   ██║    ██║  ██║█████╗      ██████╔╝█████╗     ██║   ███████╗
    ██╔══██║██║  ██║██║   ██║██║     ██╔══██║██║   ██║    ██║  ██║██╔══╝      ██╔═══╝ ██╔══╝     ██║   ╚════██║
    ██║  ██║██████╔╝╚██████╔╝╚██████╗██║  ██║╚██████╔╝    ██████╔╝███████╗    ██║     ███████╗   ██║   ███████║
    ╚═╝  ╚═╝╚═════╝  ╚═════╝  ╚═════╝╚═╝  ╚═╝ ╚═════╝     ╚═════╝ ╚══════╝    ╚═╝     ╚══════╝   ╚═╝   ╚══════╝             
                                                                                                            ''')

# Função para exibir os menus
def show_menu(menu, opcoes = True):
    global opcao
    menu_line = '==============================='
    clear_screen()
    show_title()
    print(menu_line)
    print('SEJA MUITO BEM-VINDO!')
    print(menu_line)

# Menu principal
    if (menu == 'principal'):
        print('1. Clientes')
        print('2. Animais')
        print('3. Adoções')
        print('4. Sair')
# Menu de clientes        
    elif (menu == 'cliente'):
        print('CLIENTE')
        print(menu_line)
        print('1. Novo cliente')
        print('2. Ver clientes')
        print('3. Voltar')
    elif (menu == 'novo_cliente'):
        print('NOVO CLIENTE')
    elif (menu == 'cliente_lista'):
        print('VER CLIENTES')
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
        print('3. Voltar')
    elif (menu == 'animal_adocao'):
        print('ADOTAR ANIMAL')
    elif (menu == 'animal_adotados_lista'):
        print('VER ANIMAIS ADOTADOS')
    else:
        pass

# Entrada dos menus acima
    print(menu_line)
    if opcoes:
        opcao = input('Escolha a opção desejada: ')

# Sistema de cadastros
def cadastrar(tipo):
# Cadastro de clientes
    if(tipo == 'clientes'):
        codigo = len(clientes) + 1
        nome = input('Digite o nome do cliente: ')
        email = input('Digite o e-mail do cliente: ')
# Se não existir, adicionar cliente a matriz
        clientes.append([codigo, nome, email])
# Cadastro de animais
    elif(tipo == 'animais'):
        codigo = len(animais) + 1
        nome = input('Digite o nome do animal: ')
        idade = float(input('Digite a idade do animal: '))
        raca = input('Digite a raça do animal: ')
        porte = input('Digite o porte do animal: ')
# Adicionar animal a matriz
        animais.append([codigo, nome, idade, raca, porte])
# Sistema de adoção
    elif(tipo == 'adocoes'):
        numero = len(adocoes) + 1
        cliente = int(input('Digite o código do cliente: '))
# Função para verificar se tal cliente já adotou um animal (Mais atenção pra esse parte galera)
        ja_adotou = any(adocao[1] == cliente for adocao in adocoes)
        if ja_adotou:
            print('Esse cliente já adotou um animal.')
            pressione_enter()
            return
        animal = int(input('Digite o código do animal: '))
# Adicionar o animal a matriz
        adocoes.append([numero, cliente, animal])

# Sistema de listas
def listar(tipo):
    if(tipo == 'clientes'):
        for cliente in clientes:
            print(f'Código: {cliente[0]} - Nome: {cliente[1]} - Email: {cliente[2]}')
    elif(tipo == 'animais'):
        for animal in animais:
            print(f'Código: {animal[0]} - Nome: {animal[1]} - Idade: {animal[2]} - Raça: {animal[3]} - Porte: {animal[4]}')
    elif(tipo == 'adocoes'):
        for adocao in adocoes:
            cliente = next((c for c in clientes if c[0] == adocao[1]), None)
            animal = next((a for a in animais if a[0] == adocao[2]), None)
            nome_cliente = cliente[1] if cliente else '???'
            nome_animal = animal[1] if animal else '???'
            print(f'Adoção: {adocao[0]} - Cliente: {nome_cliente} - Animal: {nome_animal}')
    else:
        print('Não há valores a exibir...')
        pressione_enter()

# Loop principal
while True:
    show_menu('principal')

# Menu de clientes
    if(opcao == '1'):
        show_menu('cliente')
        if(opcao == '1'):
            show_menu('novo_cliente', False)
            cadastrar('clientes') 
        elif(opcao == '2'):
            show_menu('cliente_lista', False)
            listar('clientes')
            pressione_enter()
        elif(opcao == '3'):
            print('VOLTAR')
        else:
            print('Opção inválida...')
# Menu de animais
    elif(opcao == '2'):
        show_menu('animal')
        if(opcao == '1'):
            show_menu('animal_cadastro', False)
            cadastrar('animais') 
        elif(opcao == '2'):
            show_menu('animal_lista', False)
            listar('animais')
            pressione_enter()
        elif(opcao == '3'):
            print('VOLTAR')
        else:
            print('Opção inválida...')
# Menu de adoções
    elif(opcao == '3'):
        show_menu('adocao')
        if(opcao == '1'):
            show_menu('animal_adocao', False)
            cadastrar('adocoes') 
        elif(opcao == '2'):
            show_menu('animal_adotados_lista', False)
            listar('adocoes')
            pressione_enter()
        elif(opcao == '3'):
            print('VOLTAR')
        else:
            print('Opção inválida...')
# Menu para voltar
    elif(opcao == '4'):
        break
    else:
        print('Opção inválida! Digite uma opção do menu...')

# Encerramento do programa
clear_screen()
print('O programa foi encerrado. Volte sempre.')