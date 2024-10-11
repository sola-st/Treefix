# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/dataset_ops.py
if self._dataset_shape.ndims == 0:
    raise ValueError("Slicing dataset elements is not supported for rank 0.")
exit(DatasetSpec(self._element_spec, self._dataset_shape[1:]))
