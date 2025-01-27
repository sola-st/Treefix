# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/tensor_array_ops_test.py
ta = tensor_array_ops.TensorArray(dtypes.float32, size=42)
ta = ta.write(0, [0])
self.assertEqual([42, 1], ta.stack().shape.as_list())
