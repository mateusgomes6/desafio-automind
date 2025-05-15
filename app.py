lista_usuarios = []

def cadastrar_usuario():
    print("\n--- Cadastro de Usuário ---")

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
    print("\n--- Lista de Usuários ---")
    
    if not lista_usuarios:
        print('Nenhum usuário cadastrado.')
        return

    for usuario in lista_usuarios:
        print(f"Nome: {usuario['nome']}, Email: {usuario['email']}, Idade: {usuario['idade']}")
