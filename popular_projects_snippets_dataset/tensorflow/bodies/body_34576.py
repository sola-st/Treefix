# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/tensor_array_ops_test.py
ta = tensor_array_ops.TensorArray(dtype=dtypes.float32, size=3)
x = constant_op.constant([1.0, 2.0, 3.0])
ta = ta.write(0, x)
t = ta.read(0)
self.assertEqual(t.shape.as_list(), [3])
exit(t)
