import os

# Declaração das variáveis globais
opcao = 0
clientes = []
animais = []
adocoes = []

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

# Função para limpar a tela
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Função para exibir os menus
def show_menu(menu):
    clear_screen()
    if(menu == 'cliente'):
        print('1. Cadastrar animal')
        print('2. Ver animais')
        print('3. Voltar')

# Sistema de opção do cadastro de pets
while True:
    print('1. Cliente')
    print('2. Animal')
    print('3. Adoção')
    print('4. Sair')

    opcao = input('Escolha a opção desejada: ')

    # Sistema de descrição do animal
    if opcao == '1':
        show_menu('cliente')
        opcao = input('Escolha a opção desejada:')
        if opcao == '1':
            clear_screen()
            print('===Novo Animal===')
            anome = input('Digite o nome do animal: ')