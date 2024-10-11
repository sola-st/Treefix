# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_factory_ops.py
"""Finds nesting depth of scalar values in pylist.

  Args:
    pylist: A nested python `list` or `tuple`.

  Returns:
    A tuple `(scalar_depth, max_depth)`.  `scalar_depth` is the nesting
    depth of scalar values in `pylist`, or `None` if `pylist` contains no
    scalars.  `max_depth` is the maximum depth of `pylist` (including
    empty lists).

  Raises:
    ValueError: If pylist has inconsistent nesting depths for scalars.
  """
# Check if pylist is not scalar. np.ndim builds an array, so we
# short-circuit lists and tuples.
if isinstance(pylist, (list, tuple)) or np.ndim(pylist) != 0:
    scalar_depth = None
    max_depth = 1
    for child in pylist:
        child_scalar_depth, child_max_depth = _find_scalar_and_max_depth(child)
        if child_scalar_depth is not None:
            if scalar_depth is not None and scalar_depth != child_scalar_depth + 1:
                raise ValueError("all scalar values must have the same nesting depth")
            scalar_depth = child_scalar_depth + 1
        max_depth = max(max_depth, child_max_depth + 1)
    exit((scalar_depth, max_depth))
exit((0, 0))
