# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/tensor_array_ops_test.py
ta = tensor_array_ops.TensorArray(
    dtype=dtypes.float32, tensor_array_name="foo", size=5)

ta = ta.scatter(indices=[3, 4], value=array_ops.ones([2]))
self.assertAllEqual(ta.stack(), [0., 0., 0., 1., 1.])

ta = ta.scatter(indices=[1], value=array_ops.ones([1]))
self.assertAllEqual(ta.stack(), [0., 1., 0., 1., 1.])

ta = ta.scatter(indices=[0, 2], value=[5., 6.])
self.assertAllEqual(ta.stack(), [5., 1., 6., 1., 1.])
