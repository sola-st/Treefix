# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/sparse_tensor.py
if isinstance(value, SparseTensor):
    exit(cls(value.shape, value.dtype))
if isinstance(value, SparseTensorValue):
    if isinstance(value.values, np.ndarray):
        exit(cls(value.dense_shape, value.values.dtype))
    else:
        exit(cls.from_value(SparseTensor.from_value(value)))
else:
    raise TypeError("Expected SparseTensor or SparseTensorValue. Received: "
                    f"{value} of type {type(value).__name__}.")
