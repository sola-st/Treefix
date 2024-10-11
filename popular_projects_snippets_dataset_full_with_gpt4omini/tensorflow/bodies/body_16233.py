# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_tensor.py
"""Return a copy of `tensors` with row_splits all having the same dtype.

  Args:
    *tensors: A list of Tensors or RaggedTensors.
    **kwargs: If 'return_dtype=True', then return a tuple (dtype, tensors),
      where `dtype` is the data type used by row-splits, and `tensors` is the
      converted list of `Tensors` and `RaggedTensors`.

  Returns:
    The converted list of `Tensors` and `RaggedTensors`.
  """
return_dtype = kwargs.pop("return_dtype", False)
if kwargs:
    raise ValueError(f"Unexpected keyword args {kwargs}.")

has_int32 = False
has_int64 = False
for tensor in tensors:
    if isinstance(tensor, RaggedTensor):
        if tensor.row_splits.dtype == dtypes.int32:
            has_int32 = True
        else:
            has_int64 = True

if has_int32 and has_int64:
    if not ragged_config.auto_cast_partition_dtype():
        raise ValueError("Input RaggedTensors have mismatched row_splits dtypes; "
                         "use RaggedTensor.with_row_splits_dtype() to convert "
                         "them to compatible dtypes.")
    dtype = dtypes.int64
    tensors = tuple(
        t.with_row_splits_dtype(dtypes.int64) if isinstance(t, RaggedTensor
                                                           ) else t
        for t in tensors)

elif has_int32:
    dtype = dtypes.int32
else:
    dtype = dtypes.int64

if return_dtype:
    exit((dtype, tensors))
else:
    exit(tensors)
