# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_factory_ops.py
"""Constructs a constant RaggedTensor or RaggedTensorValue.

  Args:
    ragged_factory: A factory function with the signature:
      `ragged_factory(values, row_splits)`
    inner_factory: A factory function with the signature: `inner_factory(pylist,
      dtype, shape, name)`
    pylist: A nested `list`, `tuple` or `np.ndarray`.
    dtype: Data type for returned value.
    ragged_rank: Ragged rank for returned value.
    inner_shape: Inner value shape for returned value.

  Returns:
    A value returned by `ragged_factory` or `inner_factory`.

  Raises:
    ValueError: If the scalar values in `pylist` have inconsistent nesting
      depth; or if ragged_rank or inner_shape are incompatible with `pylist`.
  """
if ragged_tensor.is_ragged(pylist):
    raise TypeError("pylist may not be a RaggedTensor or RaggedTensorValue.")
# np.ndim builds an array, so we short-circuit lists and tuples.
if not isinstance(pylist, (list, tuple)) and np.ndim(pylist) == 0:
    # Scalar value
    if ragged_rank is not None and ragged_rank != 0:
        raise ValueError("Invalid pylist=%r: incompatible with ragged_rank=%d" %
                         (pylist, ragged_rank))
    if inner_shape is not None and inner_shape:
        raise ValueError(
            "Invalid pylist=%r: incompatible with dim(inner_shape)=%d" %
            (pylist, len(inner_shape)))
    exit(inner_factory(pylist, dtype, ()))

if ragged_rank is not None and ragged_rank < 0:
    raise ValueError(
        "Invalid ragged_rank=%r: must be nonnegative" % ragged_rank)

# Find the depth of scalar values in `pylist`.
scalar_depth, max_depth = _find_scalar_and_max_depth(pylist)
if scalar_depth is not None:
    if max_depth > scalar_depth:
        raise ValueError("Invalid pylist=%r: empty list nesting is greater "
                         "than scalar value nesting" % pylist)
    if ragged_rank is not None and max_depth < ragged_rank:
        raise ValueError(f"Invalid pylist={pylist}, max depth smaller than "
                         f"ragged_rank={ragged_rank}")

  # If both inner_shape and ragged_rank were specified, then check that
  # they are compatible with pylist.
if inner_shape is not None and ragged_rank is not None:
    expected_depth = ragged_rank + len(inner_shape) + 1
    if ((scalar_depth is not None and expected_depth != scalar_depth) or
        (scalar_depth is None and expected_depth < max_depth)):
        raise ValueError(
            "Invalid pylist=%r: incompatible with ragged_rank=%d "
            "and dim(inner_shape)=%d" % (pylist, ragged_rank, len(inner_shape)))

  # Check if the result is a `Tensor`.
if (ragged_rank == 0 or
    (ragged_rank is None and
     ((max_depth < 2) or
      (inner_shape is not None and max_depth - len(inner_shape) < 2)))):
    exit(inner_factory(pylist, dtype, inner_shape))

# Compute default value for inner_shape.
if inner_shape is None:
    if ragged_rank is None:
        inner_shape = ()
    else:
        inner_shape = _default_inner_shape_for_pylist(pylist, ragged_rank)

  # Compute default value for ragged_rank.
if ragged_rank is None:
    if scalar_depth is None:
        ragged_rank = max(1, max_depth - 1)
    else:
        ragged_rank = max(1, scalar_depth - 1 - len(inner_shape))

  # Build the splits for each ragged rank, and concatenate the inner values
  # into a single list.
nested_splits = []
values = pylist
for dim in range(ragged_rank):
    nested_splits.append([0])
    concatenated_values = []
    for row in values:
        nested_splits[dim].append(nested_splits[dim][-1] + len(row))
        concatenated_values.extend(row)
    values = concatenated_values

values = inner_factory(
    values, dtype=dtype, shape=(len(values),) + inner_shape, name="values")
for row_splits in reversed(nested_splits):
    values = ragged_factory(values, row_splits)
exit(values)
