import sys
import csv
import os

CLIENT_TABLE = '.clients.csv'
CLIENT_SCHEMA = ['Name', 'Company', 'Email', 'Position']
clients = [] # list of clients


def _initialize_clients_from_storage():
    with open(CLIENT_TABLE, mode='r') as f:
        reader = csv.DictReader(f, fieldnames=CLIENT_SCHEMA)
        
        for row in reader:
            clients.append(row)
            
def _save_clients_to_storage():
    tmp_table_name = '{}.tmp'.format(CLIENT_TABLE)
    with open(tmp_table_name, mode='w') as f:
        writer = csv.DictWriter(f, fieldnames=CLIENT_SCHEMA)
        writer.writerows(clients)
        
        os.remove(CLIENT_TABLE)
    os.rename(tmp_table_name, CLIENT_TABLE)


def create_client(client): # create a client
    global clients
    
    if client not in clients:
        clients.append(client) # append client
    else:
        print('Client already exists in the list!')
        
   
def list_clients(): # list all clients
    
    print('uid |  name  | company  | Email  | position ')
    print('*' * 60)    
    
    for idx, client in enumerate(clients): # iterate (con la funcion enumerate)
        print('{uid} | {name} | {company} | {Email} | {position}'.format(
            uid=idx,
            name=client['Name'],
            company=client['Company'],
            Email=client['Email'],
            position=client['Position']            
        ))
        
    
def update_client(client_name, update_client_name):
    global clients
    
    if len(clients) - 1 >= client_name:
        clients[client_name] = update_client_name # index of client a modificar
    else:
        print('Client not exist!')
        
        
def delete_client(client_name):
    global clients
    
    for idx, client in enumerate(clients):
        if idx == client_name:
            del clients[idx]
            break
        
        
def search_client(client_name):
        
    for client in clients:
        if client['Name'] != client_name:
            continue
        else:
            return True
        
        
def _get_client_field(field_name, message='What is the client {}?'):
    field = None
    
    while not field:
        field = input(f'What is the client {field_name}: ')
    return field

    
def _get_client_from_user():
    client = {
        'Name': _get_client_field('name'),
        'Company': _get_client_field('company'),
        'Email': _get_client_field('Email'),
        'Position': _get_client_field('position')
    }
    
    return client


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
    _initialize_clients_from_storage()
    _print_welcome()
    
    command = input()
    # command = command.upper() no es necesario porque ya le pase la minuscula en la condicion
    
    if command == 'C' or command == 'c':
        client = _get_client_from_user()
        create_client(client)
        
    elif command == 'R' or command == 'r':        
        list_clients()
        
    elif command == 'U' or command == 'u':
        client_name = int(_get_client_field('id'))
        update_client_name = _get_client_from_user()
        
        update_client(client_name, update_client_name)
    
    elif command == 'D' or command == 'd':
        client_name = int(_get_client_field('id'))
        delete_client(client_name)        
    
    elif command == 'S' or command == 's':
        client_name = _get_client_field('name')
        found = search_client(client_name)
        
        if found:
            print('The client is in the list!')
        else:
            print(f'The client {client_name} is not in the list')    
    else:
        print('Invalid command')
        
    _save_clients_to_storage()