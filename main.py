# Declaração das variáveis globais
import os

opcao = 0
clientes = []
animais = []
adocoes = []

print('''                                                       
/ ___|(_)___| |_ ___ _ __ ___   __ _    __| | ___                    
\___ \| / __| __/ _ \ '_ ` _ \ / _` |  / _` |/ _ \                   
 ___) | \__ \ ||  __/ | | | | | (_| | | (_| |  __/                   
|____/|_|___/\__\___|_| |_| |_|\__,_|  \__,_|\___|                   
    _       _                             _        ____      _       
   / \   __| | ___   ___ __ _  ___     __| | ___  |  _ \ ___| |_ ___ 
  / _ \ / _` |/ _ \ / __/ _` |/ _ \   / _` |/ _ \ | |_) / _ \ __/ __|
 / ___ \ (_| | (_) | (_| (_| | (_) | | (_| |  __/ |  __/  __/ |_\__ \\
/_/   \_\__,_|\___/ \___\__,_|\___/   \__,_|\___| |_|   \___|\__|___/
                                                                    ''')

# Função para limpar a tela
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Sistema de opção do cadastro de pets
while True:
    print('Sistema de Cadastro de Adoção de Pets')

    print('1. Cliente')
    print('2. Animal')
    print('3. Adoção')
    print('4. Sair')

    opcao = input('Escolha a opção desejada: ')

    # Sistema de descrição do animal
    if opcao == '1':
        clear_screen()
        print('1. Cadastrar animal')
        print('2. Ver animais')
        print('3. Voltar')
        opcao = input('Escolha a opção desejada:')