import socket, sys
from concurrent.futures import ThreadPoolExecutor

def check_port(args):
    ip = args[0]
    port = args[1]
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((ip, port))
        s.close()
        print(f'{ip}:{port} is open')
        return f'{ip}:{port} is open'
    except socket.error as e:
        print(f'{ip}:{port} is close')
        return f'{ip}:{port} is close'

def f(x):
    print(x)

if __name__ == '__main__':
    li = []
    ip = '127.0.0.1'
    for i in range(1,1024):
        li.append((ip, i))
    # print(li)

    with ThreadPoolExecutor(3) as exec:
        exec.map(check_port, li)
        # exec.map(f, li)

