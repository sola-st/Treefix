# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/stateless_random_ops_test.py
for i in range(len(ls)):
    for j in range(i + 1, len(ls)):
        self.assertFalse(math_ops.reduce_all(ls[i] == ls[j]))
