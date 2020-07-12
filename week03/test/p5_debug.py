from multiprocessing import Process
import multiprocessing
import os

def debug_info(title):
    print('-'*20)
    print(title)
    print(f'模块名称 {__name__}')
    print(f'父进程 {os.getppid()}')
    print(f'当前进程 {os.getpid()}')
    print('-'*20)

def f(name):
    debug_info('function f')
    print(f'hello {name}')

if __name__ == "__main__":
    debug_info('main')
    p = Process(target=f, args=('bob',))
    p.start()

    for p in multiprocessing.active_children():
        print(f'子进程名称 {p.name},id {str(p.pid)}')
    print('进程结束')
    print(f'cpu核心数量 {str(multiprocessing.cpu_count())}')

    p.join()
