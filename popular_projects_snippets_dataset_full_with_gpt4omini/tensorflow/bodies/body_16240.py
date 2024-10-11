# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_tensor.py
"""Constructs a type specification for a `tf.RaggedTensor`.

    Args:
      shape: The shape of the RaggedTensor, or `None` to allow any shape.  If a
        shape is specified, then all ragged dimensions must have size `None`.
      dtype: `tf.DType` of values in the RaggedTensor.
      ragged_rank: Python integer, the number of times the RaggedTensor's
        flat_values is partitioned.  Defaults to `shape.ndims - 1`.
      row_splits_dtype: `dtype` for the RaggedTensor's `row_splits` tensor. One
        of `tf.int32` or `tf.int64`.
      flat_values_spec: TypeSpec for flat_value of the RaggedTensor. It shall be
        provided when the flat_values is a CompositeTensor rather then Tensor.
        If both `dtype` and `flat_values_spec` and  are provided, `dtype` must
        be the same as `flat_values_spec.dtype`. (experimental)
    """
self._shape = tensor_shape.as_shape(shape)
self._row_splits_dtype = dtypes.as_dtype(row_splits_dtype)
if flat_values_spec is not None:
    if dtype is None:
        dtype = flat_values_spec.dtype
    elif dtype != flat_values_spec.dtype:
        raise ValueError("dtype must be the same as flat_values_spec.dtype")
elif dtype is None:
    raise ValueError(
        "At least one of dtype or flat_values_spec must be provided")
self._dtype = dtypes.as_dtype(dtype)
self._flat_values_spec = flat_values_spec

rank = self._shape.ndims
if ragged_rank is None:
    if rank is None:
        raise ValueError("Must specify ragged_rank or "
                         "a shape with a known rank.")
    ragged_rank = rank - 1
self._ragged_rank = ragged_rank
if not isinstance(self._ragged_rank, int):
    raise TypeError(f"Argument `ragged_rank` must be an int. "
                    f"Received {ragged_rank}.")

if rank is not None:
    if ragged_rank >= rank:
        raise ValueError(f"Argument `ragged_rank` ({ragged_rank}) must be less "
                         f"than rank ({rank}).")
