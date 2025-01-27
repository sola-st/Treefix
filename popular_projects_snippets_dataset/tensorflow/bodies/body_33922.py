# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/v1_compat_tests/array_ops_test.py
reverse_v2 = array_ops.reverse_v2
data_t = array_ops.placeholder(dtypes.float32)
axis_known_t = array_ops.placeholder(dtypes.int32, shape=[3])
reverse_known_t = reverse_v2(data_t, axis_known_t)
# Unlike V1 we cannot know this anymore
self.assertIsNone(reverse_known_t.get_shape().ndims)

axis_unknown_t = array_ops.placeholder(dtypes.int32)
reverse_unknown_t = reverse_v2(data_t, axis_unknown_t)
self.assertIs(None, reverse_unknown_t.get_shape().ndims)

data_2d_t = array_ops.placeholder(dtypes.float32, shape=[None, None])
axis_2d_t = array_ops.placeholder(dtypes.int32, shape=[3])
reverse_2d_t = reverse_v2(data_2d_t, axis_2d_t)
self.assertEqual(2, reverse_2d_t.get_shape().ndims)
