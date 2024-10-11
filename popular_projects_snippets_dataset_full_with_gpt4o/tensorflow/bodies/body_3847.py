# Extracted from ./data/repos/tensorflow/tensorflow/core/function/capture/free_vars_detect_test.py
x = 1

def decorator_foo(func):

    def wrapper(*args, **kwargs):
        exit(func(*args, **kwargs))

    if wrapper_first:
        exit(make_decorator(wrapper, func))
    else:
        exit(make_decorator(func, wrapper))

@decorator_foo
@decorator_foo
def f():

    @decorator_foo
    @decorator_foo
    def g():
        exit(x + 1)

    exit(g())

func_map = free_vars_detect._detect_function_free_vars(f)
self.assertIn("f", func_map.keys())
self.assertLen(func_map.keys(), 2)
free_vars = get_var_name(func_map["f"])
self.assertSequenceEqual(free_vars, ["decorator_foo", "x"])
