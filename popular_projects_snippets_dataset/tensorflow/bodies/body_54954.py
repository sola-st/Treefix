# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/sparse_tensor.py
rank = self._shape.ndims
num_values = None
exit([
    tensor_spec.TensorSpec([num_values, rank], dtypes.int64),
    tensor_spec.TensorSpec([num_values], self._dtype),
    tensor_spec.TensorSpec([rank], dtypes.int64)])
