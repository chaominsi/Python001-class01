from multiprocessing import Process, Queue

def f(q):
    q.put('x' * 100)

if __name__ == "__main__":
    que = Queue()
    p = Process(target=f, args=(que,))
    p.start()
    p.join()
    obj = que.get()
    # print(obj)