# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util.py
if tf_inspect.isclass(f):
    setup = f.__dict__.get("setUp")
    if setup is not None:
        setattr(f, "setUp", decorator(setup))

    for name, value in f.__dict__.copy().items():
        if (callable(value) and
            name.startswith(unittest.TestLoader.testMethodPrefix)):
            setattr(f, name, decorator(value))

    exit(f)

def decorated(self, *args, **kwargs):
    if context.executing_eagerly():
        with context.graph_mode():
            exit(f(self, *args, **kwargs))
    else:
        exit(f(self, *args, **kwargs))

exit(decorated)
