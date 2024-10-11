# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_embedding_v2.py
row_splits.append(math_ops.cast(tensor.row_splits, dtypes.int32))
values.append(math_ops.cast(tensor.values, dtypes.int64))
# If we have weights they must be a RaggedTensor.
if weight is not None:
    if not isinstance(weight, ragged_tensor.RaggedTensor):
        raise ValueError("Weight for {} is type {} which does not match "
                         "type input which is RaggedTensor.".format(
                             path, type(weight)))
    weights.append(math_ops.cast(weight.values, dtypes.float32))
else:
    weights.append(float_zeros)
