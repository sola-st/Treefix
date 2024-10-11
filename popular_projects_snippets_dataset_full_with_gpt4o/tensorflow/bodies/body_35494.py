# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/random_binomial_test.py
rng = stateful_random_ops.Generator.from_seed(12345)
# Scalar parameters.
rnd = rng.binomial(shape=[10], counts=np.float32(2.), probs=np.float32(0.5))
self.assertEqual([10], rnd.shape.as_list())
rnd = rng.binomial(shape=[], counts=np.float32(2.), probs=np.float32(0.5))
self.assertEqual([], rnd.shape.as_list())

# Vector parameters.
rnd = rng.binomial(
    shape=[10],
    counts=array_ops.ones([10], dtype=np.float32),
    probs=0.3 * array_ops.ones([10], dtype=np.float32))
self.assertEqual([10], rnd.shape.as_list())
rnd = rng.binomial(
    shape=[5, 2],
    counts=array_ops.ones([2], dtype=np.float32),
    probs=0.4 * array_ops.ones([2], dtype=np.float32))
self.assertEqual([5, 2], rnd.shape.as_list())

# Scalar counts, vector probs.
rnd = rng.binomial(
    shape=[10],
    counts=np.float32(5.),
    probs=0.8 * array_ops.ones([10], dtype=np.float32))
self.assertEqual([10], rnd.shape.as_list())

# Vector counts, scalar probs.
rnd = rng.binomial(
    shape=[10],
    counts=array_ops.ones([10], dtype=np.float32),
    probs=np.float32(0.9))
self.assertEqual([10], rnd.shape.as_list())

# Tensor parameters
rnd = rng.binomial(
    shape=[10, 2, 3],
    counts=array_ops.ones([2, 1], dtype=np.float32),
    probs=0.9 * array_ops.ones([1, 3], dtype=np.float32))
self.assertEqual([10, 2, 3], rnd.shape.as_list())

# Tensor parameters
rnd = rng.binomial(
    shape=[10, 2, 3, 5],
    counts=array_ops.ones([2, 1, 5], dtype=np.float32),
    probs=0.9 * array_ops.ones([1, 3, 1], dtype=np.float32))
self.assertEqual([10, 2, 3, 5], rnd.shape.as_list())
