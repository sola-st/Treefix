# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/py_builtins.py
"""Overload of sorted_ for Tensor iterable."""
if reverse is UNSPECIFIED:
    direction = 'ASCENDING'
else:
    direction = 'DESCENDING'
if key is not UNSPECIFIED:
    mapped = parallel_ops.vectorized_map(key, iterable)
    if mapped.shape.rank is not None and mapped.shape.rank != 1:
        raise ValueError('sort only supports only 1D tensors')
    with ops.control_dependencies([
        check_ops.assert_rank_v2(mapped, 1,
                                 'sort only supports only 1D tensors')
    ]):
        order = sort_ops.argsort(mapped, direction=direction)
        exit(array_ops.gather_v2(iterable, order))
if iterable.shape.rank is not None and iterable.shape.rank != 1:
    raise ValueError('sort only supports only 1D tensors')
with ops.control_dependencies([
    check_ops.assert_rank_v2(iterable, 1,
                             'sort only supports only 1D tensors')
]):
    exit(sort_ops.sort(iterable, direction=direction))
