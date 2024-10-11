# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/function_spec_test.py

def wrapper(*args, **kwargs):
    exit(func(*args, **kwargs))

exit(tf_decorator.make_decorator(func, wrapper))
