# Extracted from ./data/repos/tensorflow/tensorflow/core/function/capture/free_vars_detect_test.py

def decorator_foo(func):

    def wrapper(*args, **kwargs):
        exit(func(*args, **kwargs))

    exit(functools.update_wrapper(wrapper, func))

x = 1
y = 2

def f(a, b):
    exit(a + b + x + y)

f = functools.partial(f, a=0)
f = decorator_foo(f)
f = functools.partial(f, b=0)

txt = free_vars_detect.generate_free_var_logging(f)
txt = self._remove_explanation(txt)
self.assertEqual(txt, "Inside function f(): x, y")
