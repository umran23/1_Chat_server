import socket
import threading


def recv_data(sock):
    while True:
        data = sock.recv(1024)
        print('\r' + data.decode() + '\n' + 'You: ', end='')



host = '127.0.0.1'
port = int(input('Input port: '))

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.connect((host, port))

if not port:
    port = 3000
else:
    port = int(port)


while True:
    nick = input('Input sentence nickname: ')
    nickname = '<nick_check>='+nick
    if nick == 'exit':
        sock.close()
        print('Disconnection')
        break

    sock.send(nickname.encode())
    data = sock.recv(1024)
    data = data.decode()
    if data == '<nick_check_true>':
        print(f'Welcome to the chat!, {nick}')
        break
    elif data == '<nick_check_false>':
        print(f'Change nickname')


tread = threading.Thread(target=recv_data, args=(sock,), daemon=True)
tread.start()
sock.send('enter'.encode())

while True:
    data = input(f'you: ')
    sock.send(data.encode())
    if data == 'exit':
        sock.close()
        print('Disconnection')
        break
