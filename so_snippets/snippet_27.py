# Extracted from https://stackoverflow.com/questions/1132941/least-astonishment-and-the-mutable-default-argument
def foo(arg=something_expensive_to_compute())):
    ...

funcs = [ lambda i=i: i for i in range(10)]

def make_func(i): return lambda: i
funcs = [make_func(i) for i in range(10)]

def foo(a='test', b=100, c=[]):
   print a,b,c

inspect.getargspec(foo)
(['a', 'b', 'c'], None, None, ('test', 100, []))

_undefined = object()  # sentinel value

def foo(a=_undefined, b=_undefined, c=_undefined)
    if a is _undefined: a='test'
    if b is _undefined: b=100
    if c is _undefined: c=[]

