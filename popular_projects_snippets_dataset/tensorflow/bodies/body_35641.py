# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/stateful_random_ops_test.py
if new_g[0] is None:  # avoid creating variable in 2nd trace
    new_g[0] = g.split(2)
exit([new_g[0][i].normal([]) for i in range(2)])
