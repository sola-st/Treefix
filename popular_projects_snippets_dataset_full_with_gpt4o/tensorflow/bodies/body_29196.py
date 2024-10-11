# Extracted from ./data/repos/tensorflow/tensorflow/python/data/util/nest_test.py
self.assertFalse(nest.is_nested("1234"))
self.assertFalse(nest.is_nested([1, 3, [4, 5]]))
self.assertTrue(nest.is_nested(((7, 8), (5, 6))))
self.assertFalse(nest.is_nested([]))
self.assertFalse(nest.is_nested(set([1, 2])))
ones = array_ops.ones([2, 3])
self.assertFalse(nest.is_nested(ones))
self.assertFalse(nest.is_nested(math_ops.tanh(ones)))
self.assertFalse(nest.is_nested(np.ones((4, 5))))
self.assertTrue(nest.is_nested({"foo": 1, "bar": 2}))
self.assertFalse(
    nest.is_nested(sparse_tensor.SparseTensorValue([[0]], [0], [1])))
self.assertFalse(
    nest.is_nested(ragged_factory_ops.constant_value([[[0]], [[1]]])))
