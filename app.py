lista_usuarios = []

def cadastrar_usuario():
    print('\n--- Cadastro de Usuário ---')

    nome = input('Nome: ')
    email = input('Email: ')
    idade = int(input('Idade: '))

    # Verifica se o usuário já existe
    for usuario in lista_usuarios:
        if usuario['nome'] == nome:
            print('Usuário já cadastrado.')
            return
    # Verifica se o email já existe
    for usuario in lista_usuarios:
        if usuario['email'] == email:
            print('Email já cadastrado.')
            return
        
    usuario = {
        'nome': nome,
        'email': email,
        'idade': idade
    }

    lista_usuarios.append(usuario)
    return usuario

def listar_usuarios():
    print('\n--- Lista de Usuários ---')

    if not lista_usuarios:
        print('Nenhum usuário cadastrado.')
        return

    for usuario in lista_usuarios:
        print(f"Nome: {usuario['nome']}, Email: {usuario['email']}, Idade: {usuario['idade']}")

def buscar_usuario():
    print('\n--- Buscar Usuário ---')
    nome_busca = input('Digite o nome do usuário: ').strip().lower

    for usuario in lista_usuarios:
        if usuario['nome'].strip().lower() == nome_busca:
            print(f"Nome: {usuario['nome']}, Email: {usuario['email']}, Idade: {usuario['idade']}")
            return
    print('Usuário não encontrado.')

def excluir_usuario():
    print('\n--- Excluir Usuário ---')
    nome_excluir = input('Digite o nome do usuário a ser excluído: ').strip().lower()

    for usuario in lista_usuarios:
        if usuario['nome'].strip().lower() == nome_excluir:
            lista_usuarios.remove(usuario)
            print('Usuário excluído com sucesso.')
            return
    print('Usuário não encontrado.')

def menu():
    while True:
        print('\n--- Menu ---')
        print('1. Cadastrar Usuário')
        print('2. Listar Usuários')
        print('3. Buscar Usuário')
        print('4. Excluir Usuário')
        print('5. Sair')

        opcao = input('Escolha uma opção: ')

        if opcao == '1':
            cadastrar_usuario()
        elif opcao == '2':
            listar_usuarios()
        elif opcao == '3':
            buscar_usuario()
        elif opcao == '4':
            excluir_usuario()
        elif opcao == '5':
            print('Saindo...')
            break
        else:
            print('Opção inválida. Tente novamente.')

if __name__ == '__main__':
    menu()

    
