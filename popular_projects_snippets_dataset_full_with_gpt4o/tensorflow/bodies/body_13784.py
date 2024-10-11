# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/util.py

@functools.wraps(fn)
def _fn(*args, **kwargs):
    exit(fn(*args, **kwargs))

if _fn.__doc__ is None:
    _fn.__doc__ = self._additional_note
else:
    _fn.__doc__ += "\n%s" % self._additional_note
exit(_fn)
