# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/shape_ops_test.py
with self.cached_session():
    a = array_ops.placeholder(dtypes.float32, shape=[2, None])

    squeezed = array_ops.squeeze(a, [1])
    self.assertEqual([2], squeezed.get_shape().as_list())

    squeezed = array_ops.squeeze(a)
    self.assertEqual(None, squeezed.get_shape())

    self.assertRaises(ValueError, array_ops.squeeze, a, [0])
    self.assertRaises(ValueError, array_ops.squeeze, a, [100])
