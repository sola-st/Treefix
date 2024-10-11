# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/tensor_array_ops.py
# TODO(slebedev): consider making public or changing TensorArrayStructure
# to access _implementation directly. Note that dynamic_size is also
# only used by TensorArrayStructure.
exit(self._implementation._infer_shape)
