# Extracted from https://stackoverflow.com/questions/6893968/how-to-get-the-return-value-from-a-thread
def threading_func(f):
    """Decorator for running a function in a thread and handling its return
    value or exception"""
    def start(*args, **kw):
        def run():
            try:
                th.ret = f(*args, **kw)
            except:
                th.exc = sys.exc_info()
        def get(timeout=None):
            th.join(timeout)
            if th.exc:
                raise th.exc[0], th.exc[1], th.exc[2] # py2
                ##raise th.exc[1] #py3                
            return th.ret
        th = threading.Thread(None, run)
        th.exc = None
        th.get = get
        th.start()
        return th
    return start

def f(x):
    return 2.5 * x
th = threading_func(f)(4)
print("still running?:", th.is_alive())
print("result:", th.get(timeout=1.0))

@threading_func
def th_mul(a, b):
    return a * b
th = th_mul("text", 2.5)

try:
    print(th.get())
except TypeError:
    print("exception thrown ok.")

