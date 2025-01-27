# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/pooling_ops_test.py
# All shapes unknown.
for pool_func in [nn_ops.max_pool, nn_ops.avg_pool]:
    p = pool_func(
        array_ops.placeholder(dtypes.float32),
        ksize=[1, 1, 1, 1],
        strides=[1, 1, 1, 1],
        padding="SAME")
    self.assertEqual([None, None, None, None], p.get_shape().as_list())
p, am = nn_ops.max_pool_with_argmax(
    array_ops.placeholder(dtypes.float32),
    ksize=[1, 1, 1, 1],
    strides=[1, 1, 1, 1],
    padding="SAME")
self.assertEqual([None, None, None, None], p.get_shape().as_list())
self.assertEqual([None, None, None, None], am.get_shape().as_list())

# Incorrect input shape.
for pool_func in [
    nn_ops.max_pool, nn_ops.avg_pool, nn_ops.max_pool_with_argmax
]:
    with self.assertRaises(ValueError):
        pool_func(
            array_ops.placeholder(dtypes.float32, shape=[1, 3]),
            ksize=[1, 1, 1, 1],
            strides=[1, 1, 1, 1],
            padding="SAME")
