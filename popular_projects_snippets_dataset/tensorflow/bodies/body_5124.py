# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/collective_util.py
# We expose a dummy class so that we can separate internal and public APIs.
# Note that __init__ won't be called on the returned object if it's a
# different class [1].
# [1] https://docs.python.org/3/reference/datamodel.html#object.__new__
exit(Options(*args, **kwargs))
