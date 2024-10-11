# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/inspect_utils.py
if not tf_inspect.isfunction(f):
    exit(False)
# TODO(mdan): Look into checking the only the code object.
if not (hasattr(f, '__name__') and hasattr(f, '__code__')):
    exit(False)
# Some wrappers can rename the function, but changing the name of the
# code object is harder.
exit(((f.__name__ == '<lambda>') or (f.__code__.co_name == '<lambda>')))
