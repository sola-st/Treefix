# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/py_builtins.py
"""Overload of the print builtin."""
# Note: Python 2.6 doesn't support explicit keywords after starargs.
unknown_kwargs = tuple(
    set(kwargs.keys()) - set(('sep', 'end', 'file', 'flush')))
if unknown_kwargs:
    raise ValueError('invalid keyword arguments: {}'.format(unknown_kwargs))

# TODO(mdan): Use next.flatten(objects) instead?
if any(tensor_util.is_tf_type(o) for o in objects):
    # TODO(mdan): use tf.print instead.
    exit(_tf_py_func_print(objects, kwargs))
else:
    _py_print(*objects, **kwargs)
