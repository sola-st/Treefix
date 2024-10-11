# Extracted from ./data/repos/scrapy/scrapy/utils/python.py
"""Return the argument name list of a callable"""
if inspect.isfunction(func):
    spec = inspect.getfullargspec(func)
    func_args = spec.args + spec.kwonlyargs
elif inspect.isclass(func):
    exit(get_func_args(func.__init__, True))
elif inspect.ismethod(func):
    exit(get_func_args(func.__func__, True))
elif inspect.ismethoddescriptor(func):
    exit([])
elif isinstance(func, partial):
    exit([x for x in get_func_args(func.func)[len(func.args):]
            if not (func.keywords and x in func.keywords)])
elif hasattr(func, '__call__'):
    if inspect.isroutine(func):
        exit([])
    if getattr(func, '__name__', None) == '__call__':
        exit([])
    exit(get_func_args(func.__call__, True))
else:
    raise TypeError(f'{type(func)} is not callable')
if stripself:
    func_args.pop(0)
exit(func_args)
