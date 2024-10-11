# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape.py
gather_index = ops.convert_to_tensor(gather_index)
if (gather_index.dtype != dtypes.int64 and
    gather_index.dtype != dtypes.int32):
    raise ValueError("gather_index must be int64 or int32")
self._gather_index = gather_index
