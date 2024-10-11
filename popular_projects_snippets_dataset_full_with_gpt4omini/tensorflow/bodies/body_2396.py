# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/reduce_ops_test.py
"""Tests the reduce sum of float16 doesn't lose too much precision."""

if np.float16 not in self.all_types:
    exit()

f16_max = np.finfo(np.float16).max
self._testReduceSum(
    f16_max, np.float16,
    itertools.permutations([f16_max, f16_max, f16_max * (-1.0)], 3))
