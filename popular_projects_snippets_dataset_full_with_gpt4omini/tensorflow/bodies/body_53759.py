# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util.py

def bound_f():
    f(*args, **kwds)

with context.eager_mode():
    # Running in eager mode
    bound_f()
    # Running as TF function
    # TODO(b/121143941): Remove the autograph override.
    def_function.function(bound_f, autograph=False)()
