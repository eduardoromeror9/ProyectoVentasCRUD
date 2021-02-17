primero = """import sys

clients = [
    {
        'Name': 'Eduardo',
        'Company': 'Google',
        'Email': 'eduardo@google.com',
        'Position': 'Software engineer'
    },
    {
        'Name': 'Hector',
        'Company': 'Facebook',
        'Email': 'hector@facebook.com',
        'Position': 'Data engineer'
    }
] # list of clients

def create_client(client): # create a client
    global clients
    
    if client not in clients:
        clients.append(client) # append client
    else:
        print('Client already exists in the list!')
   
def list_clients(): # list all clients
    for idx, client in enumerate(clients): # iterate (con la funcion enumerate)
        print('{uid} | {name} | {company} | {email} | {position}'.format(
            uid=idx,
            name=client['Name'],
            company=client['Company'],
            email=client['Email'],
            position=client['Position']            
        ))
    
def update_client(client_name, update_client_name):
    global clients
    
    if client_name in clients:
        index = clients.index(client_name) # index of client a modificar
        clients[index] = update_client_name # update client name and id (idx)
    else:
        print('Client is not in the list!')
        
def delete_client(client_name):
    global clients
    
    if client_name in clients:
        clients.remove(client_name) # remove client
    else:
        print('Client is not in the list!')
        
def search_client(client_name):
        
    for client in clients:
        if client != client_name:
            continue
        else:
            return True
        
def _get_client_field(field_name):
    field = None
    
    while not field:
        field = input(f'What is the client {field_name}: ')
    return field
    
def _get_client_name():
    client_name = None # get client name inicia en None
    
    while not client_name:
        client_name = input('What is the client name? ')
        
        if client_name == 'exit' or client_name == 'Exit':
            client_name = None
            break
        
    if not client_name:
        sys.exit()
        
    return client_name

def _print_welcome(): # list of commands
    print('Welcome to Eduardo VENTAS!')
    print('*' * 65)
    print('What would you like to do today?')
    print('[C]reate client')
    print('[R]ead client')
    print('[U]pdate client')
    print('[D]elete client')
    print('[S]earch client')     

if __name__ == '__main__':
    _print_welcome()
    
    command = input()
    # command = command.upper() no es necesario porque ya le pase la minuscula en la condicion
    
    if command == 'C' or command == 'c':
        client = {
            'Name': _get_client_field('Name'),
            'Company': _get_client_field('Company'),
            'Email': _get_client_field('Email'),
            'Position': _get_client_field('Position')
        }
        create_client(client)
        list_clients()
        
    elif command == 'R' or command == 'r':        
        list_clients()
        
    elif command == 'U' or command == 'u':
        client_name = _get_client_name()
        update_client_name = input('What is the update client name? ')
        
        update_client(client_name, update_client_name)
        list_clients()
    
    elif command == 'D' or command == 'd':
        client_name = _get_client_name()
        delete_client(client_name)
        list_clients()        
    
    elif command == 'S' or command == 's':
        client_name = _get_client_name()
        found = search_client(client_name)
        
        if found:
            print('The client is in the list!')
        else:
            print(f'The client {client_name} is not in the list')    
    else:
        print('Invalid command')"""
        
print('########## Segundo ##########')

import sys


clients = [
    {
        'name': 'Eduardo',
        'company': 'Google',
        'email': 'eduardo@google.com',
        'position': 'Software Engineer',
    },
    {
        'name': 'Ricardo',
        'company': 'Facebook',
        'email': 'ricardo@facebook.com',
        'position': 'Data Engineer',
    },
]


def create_client(client):
    global clients

    if client not in clients:
        clients.append(client)
    else:
        print('Client already in client\'s list')


def list_clients():
    print('uid |  name  | company  | email  | position ')
    print('*' * 60)

    for idx, client in enumerate(clients):
        print('{uid} | {name} | {company} | {email} | {position}'.format(
            uid=idx, 
            name=client['name'], 
            company=client['company'], 
            email=client['email'], 
            position=client['position']))


def update_client(client_id, updated_client):
    global clients

    if len(clients) - 1 >= client_id:
        clients[client_id] = updated_client
    else:
        print('Client not in client\'s list')


def delete_client(client_id):
    global clients

    for idx, client in enumerate(clients):
        if idx == client_id:
            del clients[idx] 
            break


def search_client(client_name):
    for client in clients:
        if client['name'] != client_name:
            continue
        else:
            return True


def _get_client_field(field_name, message='What is the client {}?'):
    field = None

    while not field:
        field = input(message.format(field_name))

    return field


def _get_client_from_user():
    client = {
        'name': _get_client_field('name'),
        'company': _get_client_field('company'),
        'email': _get_client_field('email'),
        'position': _get_client_field('position'),
    }

    return client


def _print_welcome():
    print('WELCOME TO PLATZI VENTAS')
    print('*' * 50)
    print('What would you like to do today?:')
    print('[C]reate client')
    print('[L]ist clients')
    print('[U]pdate client')
    print('[D]elete client')
    print('[S]earch client')


if __name__ == '__main__':
    _print_welcome()

    command = input()
    command = command.upper()

    if command == 'C':
        client = _get_client_from_user()

        create_client(client)
        list_clients()
    elif command == 'L':
        list_clients()
    elif command == 'U':
        client_id = int(_get_client_field('id'))
        updated_client = _get_client_from_user()

        update_client(client_id, updated_client)
        list_clients()
    elif command == 'D':
        client_id = int(_get_client_field('id'))

        delete_client(client_id)
        list_clients()
    elif command == 'S':
        client_name = _get_client_field('name')
        found = search_client(client_name)
        
        if found:
            print('The client is in the client\'s list')
        else:
            print('The client: {} is not in our client\'s list'.format(client_name))
    else:
        print('Invalid command')