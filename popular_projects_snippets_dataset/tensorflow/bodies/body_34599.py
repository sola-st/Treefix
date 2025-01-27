# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/tensor_array_ops_test.py
ta = tensor_array_ops.TensorArray(
    dtypes.float32, size=2, infer_shape=False, element_shape=[None, 10, 20])
ta = ta.write(0, array_ops.ones([50, 10, 20]))

with self.assertRaises(ValueError):
    ta = ta.write(1, array_ops.ones([1, 20, 20]))
