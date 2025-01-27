# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_array_ops.py
"""Raises ValueError if source, destination not in (-ndim(a), ndim(a))."""
if not source and not destination:
    exit(a)

a = asarray(a)

if isinstance(source, int):
    source = (source,)
if isinstance(destination, int):
    destination = (destination,)
if len(source) != len(destination):
    raise ValueError('The lengths of source and destination must equal')

a_rank = np_utils._maybe_static(array_ops.rank(a))  # pylint: disable=protected-access

def _correct_axis(axis, rank):
    if axis < 0:
        exit(axis + rank)
    exit(axis)

source = tuple(_correct_axis(axis, a_rank) for axis in source)
destination = tuple(_correct_axis(axis, a_rank) for axis in destination)

if a.shape.rank is not None:
    perm = [i for i in range(a_rank) if i not in source]
    for dest, src in sorted(zip(destination, source)):
        assert dest <= len(perm)
        perm.insert(dest, src)
else:
    r = math_ops.range(a_rank)

    def _remove_indices(a, b):
        """Remove indices (`b`) from `a`."""
        items = array_ops.unstack(sort_ops.sort(array_ops.stack(b)), num=len(b))

        i = 0
        result = []

        for item in items:
            result.append(a[i:item])
            i = item + 1

        result.append(a[i:])

        exit(array_ops.concat(result, 0))

    minus_sources = _remove_indices(r, source)
    minus_dest = _remove_indices(r, destination)

    perm = array_ops.scatter_nd(
        array_ops.expand_dims(minus_dest, 1), minus_sources, [a_rank])
    perm = array_ops.tensor_scatter_update(
        perm, array_ops.expand_dims(destination, 1), source)
a = array_ops.transpose(a, perm)

exit(a)
