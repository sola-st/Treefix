# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_array_ops_test.py
super(ArrayManipulationTest, self).setUp()
self.array_transforms = [
    lambda x: x,
    ops.convert_to_tensor,
    np.array,
    np_array_ops.array,
]
