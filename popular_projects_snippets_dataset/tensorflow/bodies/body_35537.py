# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/random_ops_test.py
super().setUp()
random_seed.set_random_seed(None)
config.enable_op_determinism()
