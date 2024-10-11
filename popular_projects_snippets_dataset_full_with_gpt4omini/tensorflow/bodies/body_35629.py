# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/random_poisson_test.py
# Fully known shape
rnd = random_ops.random_poisson(2.0, [150], seed=12345)
self.assertEqual([150], rnd.get_shape().as_list())
rnd = random_ops.random_poisson(
    lam=array_ops.ones([1, 2, 3]),
    shape=[150],
    seed=12345)
self.assertEqual([150, 1, 2, 3], rnd.get_shape().as_list())
rnd = random_ops.random_poisson(
    lam=array_ops.ones([1, 2, 3]),
    shape=[20, 30],
    seed=12345)
self.assertEqual([20, 30, 1, 2, 3], rnd.get_shape().as_list())
rnd = random_ops.random_poisson(
    lam=array_ops.placeholder(dtypes.float32, shape=(2,)),
    shape=[12],
    seed=12345)
self.assertEqual([12, 2], rnd.get_shape().as_list())
# Partially known shape.
rnd = random_ops.random_poisson(
    lam=array_ops.ones([7, 3]),
    shape=array_ops.placeholder(dtypes.int32, shape=(1,)),
    seed=12345)
self.assertEqual([None, 7, 3], rnd.get_shape().as_list())
rnd = random_ops.random_poisson(
    lam=array_ops.ones([9, 6]),
    shape=array_ops.placeholder(dtypes.int32, shape=(3,)),
    seed=12345)
self.assertEqual([None, None, None, 9, 6], rnd.get_shape().as_list())
# Unknown shape.
rnd = random_ops.random_poisson(
    lam=array_ops.placeholder(dtypes.float32),
    shape=array_ops.placeholder(dtypes.int32),
    seed=12345)
self.assertIs(None, rnd.get_shape().ndims)
rnd = random_ops.random_poisson(
    lam=array_ops.placeholder(dtypes.float32),
    shape=[50],
    seed=12345)
self.assertIs(None, rnd.get_shape().ndims)
