# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/dataset_ops.py
if self._dataset_shape.ndims == 0:
    raise ValueError("Slicing dataset elements is not supported for rank 0.")
exit(self._to_tensor_list(value))
