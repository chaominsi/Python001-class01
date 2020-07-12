from multiprocessing import Process

def f(name):
    print(f'hello {name}')

if __name__ == "__main__":
    
    p = Process(target=f, args=('join',))
    p.start()
    p.join()