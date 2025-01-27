# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/random_gamma_test.py
# Fully known shape.
rnd = random_ops.random_gamma([150], 2.0)
self.assertEqual([150], rnd.get_shape().as_list())
rnd = random_ops.random_gamma([150], 2.0, beta=[3.0, 4.0])
self.assertEqual([150, 2], rnd.get_shape().as_list())
rnd = random_ops.random_gamma([150], array_ops.ones([1, 2, 3]))
self.assertEqual([150, 1, 2, 3], rnd.get_shape().as_list())
rnd = random_ops.random_gamma([20, 30], array_ops.ones([1, 2, 3]))
self.assertEqual([20, 30, 1, 2, 3], rnd.get_shape().as_list())
rnd = random_ops.random_gamma(
    [123], array_ops.placeholder(
        dtypes.float32, shape=(2,)))
self.assertEqual([123, 2], rnd.get_shape().as_list())
# Partially known shape.
rnd = random_ops.random_gamma(
    array_ops.placeholder(
        dtypes.int32, shape=(1,)), array_ops.ones([7, 3]))
self.assertEqual([None, 7, 3], rnd.get_shape().as_list())
rnd = random_ops.random_gamma(
    array_ops.placeholder(
        dtypes.int32, shape=(3,)), array_ops.ones([9, 6]))
self.assertEqual([None, None, None, 9, 6], rnd.get_shape().as_list())
# Unknown shape.
rnd = random_ops.random_gamma(
    array_ops.placeholder(dtypes.int32),
    array_ops.placeholder(dtypes.float32))
self.assertIs(None, rnd.get_shape().ndims)
rnd = random_ops.random_gamma([50], array_ops.placeholder(dtypes.float32))
self.assertIs(None, rnd.get_shape().ndims)
