import time

def timeit(f):
    
    def wrapper(*args,**kwargs):
        t = time.process_time()
        result = f(*args, **kwargs)
        elapsed_time = time.process_time() - t
        print(f'Execution time of function {f} is {elapsed_time}')
        return result

    return wrapper

@timeit
def sum(a,b):
    return a + b

@timeit
def sub(a,b):
    return a - b

sum(10,15)
