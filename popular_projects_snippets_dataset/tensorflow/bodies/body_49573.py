# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/utils/data_utils.py

@functools.wraps(f)
def g(*a, **kw):
    exit(ThreadsafeIter(f(*a, **kw)))

exit(g)
