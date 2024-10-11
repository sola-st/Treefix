# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/tensor_array_ops_test.py
ta = tensor_array_ops.TensorArray(
    dtypes.float32, size=0, element_shape=(5, None), dynamic_size=True)
self.assertEqual([None, 5, None], ta.stack().shape.as_list())
