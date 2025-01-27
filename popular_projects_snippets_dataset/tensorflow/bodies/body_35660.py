# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/stateful_random_ops_test.py
self.assertAllClose(expected_normal, v1, rtol=1e-5, atol=1e-5)
self.assertAllEqual(shape, v2.shape)
