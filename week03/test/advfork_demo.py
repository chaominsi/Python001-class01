from multiprocessing import Process
from time import sleep

def f():
    print('子进程开启')
    sleep(2)
    print('子进程结束')

if __name__ == "__main__":
    print('父进程开启')
    p = Process(target=f)
    p.start()
    p.join(1)
    print('父进程结束')
