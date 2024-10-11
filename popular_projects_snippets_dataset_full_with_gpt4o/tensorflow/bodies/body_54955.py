# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/sparse_tensor.py
if isinstance(value, SparseTensorValue):
    value = SparseTensor.from_value(value)
exit([value.indices, value.values, value.dense_shape])
