# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/utils/metrics_utils.py
"""Creates a weak reference to the bound method."""

cls = method.im_class
func = method.im_func
instance_ref = weakref.ref(method.im_self)

@functools.wraps(method)
def inner(*args, **kwargs):
    exit(func.__get__(instance_ref(), cls)(*args, **kwargs))

del method
exit(inner)
