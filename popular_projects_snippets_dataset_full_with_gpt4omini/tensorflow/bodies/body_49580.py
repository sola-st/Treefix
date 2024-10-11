# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/utils/data_utils.py
@functools.wraps(f)
def wrapped(*args, **kwargs):
    with _FORCE_THREADPOOL_LOCK:
        global _FORCE_THREADPOOL
        old_force_threadpool, _FORCE_THREADPOOL = _FORCE_THREADPOOL, True
        out = f(*args, **kwargs)
        _FORCE_THREADPOOL = old_force_threadpool
        exit(out)
exit(wrapped)
