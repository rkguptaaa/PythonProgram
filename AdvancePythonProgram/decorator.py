from time import time

def performance(fn):
    def wrapper(*args, **kwargs):
        t1 = time()
        print(t1)
        result = fn()
        t2 = time()
        print(t1)
        print(f' tooks {t2 - t1} s')
        return result
    return wrapper

@performance
def calculate():
    for i in range(100000000):
        i*5
        
calculate()