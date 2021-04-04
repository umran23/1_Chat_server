import socket

host = '127.0.0.1'
port = 3000
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    try:
        sock.bind((host, port))
        print('Welcome to Bony Chat Server ')
        break
    except OSError:
        port += 1


usr = {}

while True:
        data, addr = sock.recvfrom(1024)
        print('Date Received')
        if data == '':
            continue

        user_id = addr[1]
        data = data.decode()
        if data == 'enter':
            print(f'Client {user_id} enter the chat')
            continue
        if '<nick_check>' in data:
            user_nick = data.split('>=')[1]
            if user_nick not in usr.values():
                usr.setdefault(addr, user_nick)
                sock.sendto('<nick_check_true>'.encode(), addr)
                continue
            else:
                sock.sendto('<nick_check_false>'.encode(), addr)
                continue

        data = f'{usr.get(addr)}: {data}'
        for user in usr:
            if user != addr:
                sock.sendto(data.encode(), user)
