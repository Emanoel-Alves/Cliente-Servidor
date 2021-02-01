import socket
import _thread
import time

HOST = 'localhost'         # Endereco IP do Servidor
PORT = 8080                # Porta que o Servidor esta

def conectado(connection, address_client):
    print ('Realizando soma dos numeros do cliente ' + str(address_client))

    start_Time = time.time()
    while True:
        message = connection.recv(1024)
        if not message: break
        
        sum = 0
        numbers = message.decode('utf8').split(' ')

        for i in numbers:
            if i != '':
                sum = sum + int(i)
    
        connection.sendall(str(sum).encode("utf8"))

    end_Time = time.time()
    print('\nFinalizado a soma da sequencia do cliente ' + str(address_client[1]) + ' em ' + str(end_Time - start_Time) + ' segundos')
    print('Fim da conexao com o cliente ' + str(address_client))

    connection.close()
    _thread.exit()

socket_service = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

socket_service.bind((HOST, PORT))
socket_service.listen(1)
print('Servidor aguardando conexao com os clientes na porta 8080\n')

while True:
    connection, address_client = socket_service.accept()
    _thread.start_new_thread(conectado, tuple([connection, address_client]))

socket_service.close()