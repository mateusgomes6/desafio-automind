lista_usuarios = []

def cadastrar_usuario():
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