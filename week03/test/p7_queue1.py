from multiprocessing import Process, Queue
import time

def f(q):
    time.sleep(2)
    q.put('asdf')

if __name__ == "__main__":
    q = Queue()
    p = Process(target=f, args=(q,))
    p.start()
    print(1111)
    print(q.get())
    print(2222)
    # p.join()
