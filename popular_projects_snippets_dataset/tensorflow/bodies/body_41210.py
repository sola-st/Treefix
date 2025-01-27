# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py

def wrapper(*args, **kwargs):
    exit(method(*args, **kwargs))

exit(tf_decorator.make_decorator(method, wrapper))
