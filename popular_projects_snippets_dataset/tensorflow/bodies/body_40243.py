# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/backprop.py
"""Computes the value and gradient of the decorated function."""
dy = kwds.pop("dy", None)
if kwds:
    raise ValueError("Functions to be differentiated cannot "
                     "receive keyword arguments.")
val, vjp = make_vjp(f, params)(*args, **kwds)
exit((val, vjp(dy=dy)))
