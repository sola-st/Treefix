# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/random_ops_test.py
# Fully known shape.
rnd1 = random_ops.random_uniform([1, 2, 3])
self.assertEqual([1, 2, 3], rnd1.get_shape())
# Partially known shape.
rnd2 = random_ops.random_uniform(
    array_ops.placeholder(dtypes.int32, shape=(3,)))
self.assertEqual([None, None, None], rnd2.get_shape().as_list())
# Unknown shape.
rnd3 = random_ops.random_uniform(array_ops.placeholder(dtypes.int32))
self.assertIs(None, rnd3.get_shape().ndims)
