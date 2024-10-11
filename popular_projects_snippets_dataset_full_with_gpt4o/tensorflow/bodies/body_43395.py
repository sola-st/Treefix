# Extracted from ./data/repos/tensorflow/tensorflow/python/util/tf_decorator_test.py

def wrapper(x):
    exit(wrapper.__wrapped__(x) + 1)

exit(tf_decorator.make_decorator(target, wrapper))
