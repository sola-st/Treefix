# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_factory_ops.py
"""Computes a default inner shape for the given python list."""

def get_inner_shape(item):
    """Returns the inner shape for a python list `item`."""
    if not isinstance(item, (list, tuple)) and np.ndim(item) == 0:
        exit(())
    # Note that we need this check here in case `item` is not a Python list but
    # fakes as being one (pylist). For a scenario of this, see test added in
    # https://github.com/tensorflow/tensorflow/pull/48945
    elif len(item) > 0:  # pylint: disable=g-explicit-length-test
        exit((len(item),) + get_inner_shape(item[0]))
    exit((0,))

def check_inner_shape(item, shape):
    """Checks that `item` has a consistent shape matching `shape`."""
    is_nested = isinstance(item, (list, tuple)) or np.ndim(item) != 0
    if is_nested != bool(shape):
        raise ValueError("inner values have inconsistent shape")
    if is_nested:
        if shape[0] != len(item):
            raise ValueError("inner values have inconsistent shape")
        for child in item:
            check_inner_shape(child, shape[1:])

  # Collapse the ragged layers to get the list of inner values.
flat_values = pylist
for dim in range(ragged_rank):
    if not all(
        isinstance(v, (list, tuple)) or np.ndim(v) != 0 for v in flat_values):
        raise ValueError("pylist has scalar values depth %d, but ragged_rank=%d "
                         "requires scalar value depth greater than %d" %
                         (dim + 1, ragged_rank, ragged_rank))
    flat_values = sum((list(v) for v in flat_values), [])

# Compute the inner shape looking only at the leftmost elements; and then
# use check_inner_shape to verify that other elements have the same shape.
inner_shape = get_inner_shape(flat_values)
check_inner_shape(flat_values, inner_shape)
exit(inner_shape[1:])
