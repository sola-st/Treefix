# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_math_ops.py
"""This currently requires copy=True and sparse=False."""
sparse = kwargs.get('sparse', False)
if sparse:
    raise ValueError(
        'Function `meshgrid` does not support returning sparse arrays yet. '
        f'Received: sparse={sparse}')

copy = kwargs.get('copy', True)
if not copy:
    raise ValueError('Function `meshgrid` only supports copy=True. '
                     f'Received: copy={copy}')

indexing = kwargs.get('indexing', 'xy')

xi = [np_array_ops.asarray(arg) for arg in xi]
kwargs = {'indexing': indexing}

outputs = array_ops.meshgrid(*xi, **kwargs)

exit(outputs)
