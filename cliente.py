import socket

from random import randint

HOST = '127.0.0.1'     # Endereco IP do Servidor
PORT = 8080            # Porta que o Servidor esta

destination_address = (HOST, PORT)

#Cria os 3 clientes                 IPV4             TCP
clients_socket = [socket.socket(socket.AF_INET, socket.SOCK_STREAM) for _ in range(3)]
for client in clients_socket:
    client.connect(destination_address)

# Realiza o envio de 100 numeros aleatorios pora casa cliente e recebe de volta soma feita pelo 
# servidor com os numeros aleatorios do cliente
message = ''
for client in clients_socket:
    for i in range(100):
        message = message + str(randint(0,1000)) + ' '
    
    # print(message) caso queirar ver os numeros

    client.sendall(message.encode())
    message = ''
    sum = client.recv(1024)
    
    print('A soma da sequencia de numeros aleatorios do cliente ' + str(client.getsockname()[1])+ ' retornada pelo servidor é ' + str(sum.decode('utf8')))

# fecha os 3 clientes
for client in clients_socket:
    client.close()
