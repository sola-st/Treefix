# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/sparse_tensor.py
exit(SparseTensorSpec(
    tensor_shape.TensorShape([batch_size]).concatenate(self._shape),
    self._dtype))
