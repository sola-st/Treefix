# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/tensor_array_ops_test.py
ta = tensor_array_ops.TensorArray(
    dtypes.float32, size=3, infer_shape=True, element_shape=[None, 10, 20])
self.assertAllEqual((None, 10, 20), ta.element_shape.as_list())
ta = ta.write(0, array_ops.ones([50, 10, 20]))
self.assertAllEqual((50, 10, 20), ta.element_shape.as_list())
ta = ta.write(1, array_ops.ones([50, 10, 20]))
with self.assertRaises(ValueError):
    ta = ta.write(
        2, array_ops.ones([1, 10, 20])
    )  # Inconsistent shapes: saw (1, 10, 20) but expected (50, 10, 20)
