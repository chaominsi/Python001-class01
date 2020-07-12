from concurrent.futures import ThreadPoolExecutor

def f(args):
    print(args)

if __name__ == "__main__":
    seed = [1,2,3,4]

    with ThreadPoolExecutor(3) as exec:
        exec.submit(f, seed)
