# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
# All inputs unknown.
p1 = array_ops.placeholder(dtypes.float32)
p2 = array_ops.placeholder(dtypes.float32)
p3 = array_ops.placeholder(dtypes.float32)
m, index = control_flow_ops.merge([p1, p2, p3])
self.assertIs(None, m.get_shape().ndims)
self.assertEqual([], index.get_shape())

# All inputs known with different ranks.
p1 = array_ops.placeholder(dtypes.float32, shape=[1, 2])
p2 = array_ops.placeholder(dtypes.float32, shape=[1, 2, 3])
m, index = control_flow_ops.merge([p1, p2])
self.assertIs(None, m.get_shape().ndims)
self.assertEqual([], index.get_shape())

# All inputs known with some dimensions different.
p1 = array_ops.placeholder(dtypes.float32, shape=[1, 2])
p2 = array_ops.placeholder(dtypes.float32, shape=[2, 1])
m, index = control_flow_ops.merge([p1, p2])
self.assertEqual([None, None], m.get_shape().as_list())
self.assertEqual([], index.get_shape())

p1 = array_ops.placeholder(dtypes.float32, shape=[1, 2])
p2 = array_ops.placeholder(dtypes.float32, shape=[None, 2])
m, index = control_flow_ops.merge([p1, p2])
self.assertEqual([None, 2], m.get_shape().as_list())
self.assertEqual([], index.get_shape())

p1 = array_ops.placeholder(dtypes.float32, shape=[1, 2])
p2 = array_ops.placeholder(dtypes.float32, shape=[2, 2])
m, index = control_flow_ops.merge([p1, p2])
self.assertEqual([None, 2], m.get_shape().as_list())
self.assertEqual([], index.get_shape())

# All inputs known with same dimensions.
p1 = array_ops.placeholder(dtypes.float32, shape=[1, 2])
p2 = array_ops.placeholder(dtypes.float32, shape=[1, 2])
m, index = control_flow_ops.merge([p1, p2])
self.assertEqual([1, 2], m.get_shape().as_list())
self.assertEqual([], index.get_shape())

p1 = array_ops.placeholder(dtypes.float32, shape=[None, 2])
p2 = array_ops.placeholder(dtypes.float32, shape=[None, 2])
m, index = control_flow_ops.merge([p1, p2])
self.assertEqual([None, 2], m.get_shape().as_list())
self.assertEqual([], index.get_shape())

p1 = array_ops.placeholder(dtypes.float32, shape=[None, None])
p2 = array_ops.placeholder(dtypes.float32, shape=[None, None])
m, index = control_flow_ops.merge([p1, p2])
self.assertEqual([None, None], m.get_shape().as_list())
self.assertEqual([], index.get_shape())
