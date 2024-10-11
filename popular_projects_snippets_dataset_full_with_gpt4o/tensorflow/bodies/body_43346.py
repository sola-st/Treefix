# Extracted from ./data/repos/tensorflow/tensorflow/python/util/tf_stack.py
super().__init__()
filter_filename = None
outer_f = None
f = inspect.currentframe()
try:
    if f is not None:
        # The current frame is __init__. The first outer frame should be the
        # caller.
        outer_f = f.f_back
        if outer_f is not None:
            filter_filename = inspect.getsourcefile(outer_f)
    self._filename = filter_filename
    # This may be called repeatedly: once on entry by the superclass, then by
    # each child context manager.
    self._cached_set = None
finally:
    # Avoid reference cycles, see:
    # https://docs.python.org/3.7/library/inspect.html#the-interpreter-stack
    del f
    del outer_f
