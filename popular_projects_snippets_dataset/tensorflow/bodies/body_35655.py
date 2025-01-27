# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/stateful_random_ops_test.py
global g_unseeded
# defun'ed function should only create variables once
if g_unseeded is None:
    g_unseeded = random.Generator.from_non_deterministic_state()
exit(g_unseeded.normal(shape))
