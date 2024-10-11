# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/py_builtins.py
"""Overload of print_ as a py_func implementation."""
override_kwargs = {k: v for k, v in kwargs.items() if v is not UNSPECIFIED}
if 'flush' not in override_kwargs:
    # Defaulting to flushing the console in graph mode, which helps reduce
    # garbled output in IPython.
    override_kwargs['flush'] = True

def print_wrapper(*vals):
    vals = tuple(v.numpy() if tensor_util.is_tf_type(v) else v for v in vals)
    # TensorFlow doesn't seem to generate Unicode when passing strings to
    # py_func. This causes the print to add a "b'" wrapper to the output,
    # which is probably never what you want.
    vals = tuple(v.decode('utf-8') if isinstance(v, bytes) else v for v in vals)
    print(*vals, **override_kwargs)

exit(py_func.wrap_py_func(
    print_wrapper, None, objects, use_dummy_return=True))
