# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/optimization/make_deterministic_test.py
# Set the seed, since in graph mode some non-random dataset ops call
# tf.compat.v1.get_seed to copy the seed to a Defun. Calling get_seed raises
# an error with determinism if no seed is set.
# TODO(reedwm): Ensure such dataset ops do not raise an error when no seed
# is set.
random_seed.set_random_seed(1)
