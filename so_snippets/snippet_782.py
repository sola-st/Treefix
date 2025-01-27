# Extracted from https://stackoverflow.com/questions/37031928/type-annotations-for-args-and-kwargs
def foo(*args: str, **kwds: int): ...

foo('a', 'b', 'c')
foo(x=1, y=2)
foo('', z=0)

def foo(*args: int):

def foo(first: int, second: Optional[int] = None):

