# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util_test.py
random_seed.set_seed(1066)
index = random_ops.random_shuffle([0, 1, 2, 3, 4], seed=2021)
# This failed when `a` and `b` were evaluated in separate sessions.
self.assertAllEqual(index, index)
