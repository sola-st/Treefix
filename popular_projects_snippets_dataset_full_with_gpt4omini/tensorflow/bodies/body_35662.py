# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/stateful_random_ops_test.py
"""A simple test to make sure the op works in eager and defunned mode."""
random.get_global_generator().normal((3,))
