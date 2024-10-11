# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_logic_test.py
super(LogicTest, self).setUp()
self.array_transforms = [
    lambda x: x,  # Identity,
    ops.convert_to_tensor,
    np.array,
    lambda x: np.array(x, dtype=np.int32),
    lambda x: np.array(x, dtype=np.int64),
    lambda x: np.array(x, dtype=np.float32),
    lambda x: np.array(x, dtype=np.float64),
    np_array_ops.array,
    lambda x: np_array_ops.array(x, dtype=dtypes.int32),
    lambda x: np_array_ops.array(x, dtype=dtypes.int64),
    lambda x: np_array_ops.array(x, dtype=dtypes.float32),
    lambda x: np_array_ops.array(x, dtype=dtypes.float64),
]
