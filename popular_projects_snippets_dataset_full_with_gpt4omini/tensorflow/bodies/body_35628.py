# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/random_poisson_test.py
with self.cached_session():
    rnd = random_ops.random_poisson([], [], seed=12345)
    self.assertEqual([0], rnd.get_shape().as_list())
    self.assertAllClose(np.array([], dtype=np.float32), self.evaluate(rnd))
