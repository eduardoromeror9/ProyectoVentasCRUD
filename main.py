import sys

clients = ['Pablo,' 'Ricardo', 'Hector', 'Miguel Eduardo', 'Caro'] # list of clients

def create_client(client_name): # create a client
    global clients
    
    if client_name not in clients:
        clients.append(client_name) # append client
    else:
        print('Client already exists in the list!')
   
def list_clients(): # list all clients
    for idx, client in enumerate(clients): # iterate (con la funcion enumerate)
        print(f'{idx}: {client}') # print client name and id (idx)
    
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
        client_name = _get_client_name()
        create_client(client_name)
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
        print('Invalid command')