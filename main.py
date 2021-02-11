clients = 'Pablo, Ricardo, Hector, Miguel Eduardo, Caro, '

def create_client(client_name):
    global clients
    
    if client_name not in clients:
        clients += client_name
        _add_comma()
    else:
        print('Client already exists in the list!')
   
def list_clients():
    global clients
    print(clients)
    
def update_client(client_name, update_client_name):
    global clients
    
    if client_name in clients:
        clients = clients.replace(client_name + ',', update_client_name + ',')
    else:
        print('Client is not in the list!')
        
def delete_client(client_name):
    global clients
    
    if client_name in clients:
        clients = clients.replace(client_name + ',' , '')
    else:
        print('Client is not in the list!')
        
def search_client(client_name):
    clients_list =  clients.split(',')
    
    for client in clients_list:
        if client != client_name:
            continue
        else:
            return True

def _add_comma():
    global clients
    clients += ','
    
def _print_welcome():
    print('Welcome to Eduardo VENTAS!')
    print('*' * 65)
    print('What would you like to do today?')
    print('[C]reate client')
    print('[R]ead client')
    print('[U]pdate client')
    print('[D]elete client')
    print('[S]earch client')
    
def _get_client_name():
    return input('What is the client name? ')    

if __name__ == '__main__':
    _print_welcome()
    
    command = input()
    # command = command.upper() no es necesario porque ya le pase la minuscula por la condicion
    
    if command == 'C' or command == 'c':
        client_name = _get_client_name()
        create_client(client_name)
        list_clients()
        
    elif command == 'R' or command == 'r':        
        list_clients()
    
    elif command == 'D' or command == 'd':
        client_name = _get_client_name()
        delete_client(client_name)
        list_clients()
        
    elif command == 'U' or command == 'u':
        client_name = _get_client_name()
        update_client_name = input('What is the update client name? ')
        update_client(client_name, update_client_name)
        list_clients()        
    
    elif command == 'S' or command == 's':
        client_name = _get_client_name()
        found = search_client(client_name)
        
        if found:
            print('The client is in the list!')
        else:
            print(f'The client {client_name} is not in the list')
    
    else:
        print('Invalid command')