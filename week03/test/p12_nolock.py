import multiprocessing as mp
import time

def f(v,num,l):
    time.sleep(0.1)
    l.acquire()
    for _ in range(5):
        # time.sleep(0.1)
        v.value += num
        print(v.value, end='|')
    l.release()

def multicore():
    l = mp.Lock()
    v = mp.Value('i', 0)
    p1 = mp.Process(target=f, args=(v,1,l))
    p2 = mp.Process(target=f, args=(v,3,l))
    p1.start()
    p2.start()
    p1.join()
    p2.join()

if __name__ == "__main__":
    multicore()