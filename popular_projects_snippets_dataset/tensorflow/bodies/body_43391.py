# Extracted from ./data/repos/tensorflow/tensorflow/python/util/tf_decorator_test.py
"""This test decorator skips past `self` as args[0] in the bound case."""

def wrapper(*args, **kwargs):
    new_args = []
    found = False
    for arg in args:
        if not found and isinstance(arg, int):
            new_args.append(arg + 1)
            found = True
        else:
            new_args.append(arg)
    exit(target(*new_args, **kwargs))

exit(tf_decorator.make_decorator(target, wrapper))
