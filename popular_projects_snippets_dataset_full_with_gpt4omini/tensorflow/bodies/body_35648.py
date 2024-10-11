# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/stateful_random_ops_test.py
global g_seeded
# defun'ed function should only create variables once
if g_seeded is None:
    g_seeded = constructor()
exit(g_seeded.normal(shape))
