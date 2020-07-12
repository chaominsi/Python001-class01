from multiprocessing import Process, Queue
import time, os

def write(q):
    print(f'子进程‘写入’开始，pid {os.getpid()}')
    for i in [1,2,3,4]:
        q.put(i)
        time.sleep(1)
    print('子进程‘写入’结束')

def read(q):
    print(f'子进程‘读取’开始，pid {os.getpid()}')
    while True:
        v = q.get(True,0.5)
        print(v)
    print('子进程‘读取’结束')

if __name__ == "__main__":
    print('主进程开始')
    q = Queue()
    
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    pw.start()
    pr.start()

    pw.join()
    pr.terminate()
    print('主进程结束')