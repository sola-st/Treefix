# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util_test.py
# Call setUp again for WithCApi case (since it makes a new default graph
# after setup).
# TODO(skyewm): remove this when C API is permanently enabled.
with context.eager_mode():
    self.setUp()
    a = random.randint(1, 1000)
    a_np_rand = np.random.rand(1)
    a_rand = random_ops.random_normal([1])
    # ensure that randomness in multiple testCases is deterministic.
    self.setUp()
    b = random.randint(1, 1000)
    b_np_rand = np.random.rand(1)
    b_rand = random_ops.random_normal([1])
    self.assertEqual(a, b)
    self.assertEqual(a_np_rand, b_np_rand)
    self.assertAllEqual(a_rand, b_rand)
