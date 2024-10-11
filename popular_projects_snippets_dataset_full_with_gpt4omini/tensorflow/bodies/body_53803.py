# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util.py

def decorator(func):

    def decorated(self, *args, **kwargs):
        if execute_func:
            exit(func(self, *args, **kwargs))

    exit(tf_decorator.make_decorator(func, decorated))

if func is not None:
    exit(decorator(func))

exit(decorator)
