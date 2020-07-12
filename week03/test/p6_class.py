# from multiprocessing import Process

# 不指定target时，默认执行Process类中的run方法
# if __name__ == "__main__":
#     p = Process()             # 啥也没有

from multiprocessing import Process
import os, time

class NewProcess(Process):
    def __init__(self,num):
        self.num = num
        super().__init__()
    
    def run(self):
        print(f'我是进程 {self.num},进程名 {self.name}, 进程id {os.getpid(), self.pid}, 父进程id {os.getppid()}')
        time.sleep(2)

if __name__ == "__main__":
    print("start")
    for i in range(2):
        p = NewProcess(i)
        p.start()
    print('end')
