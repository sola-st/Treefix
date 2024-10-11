# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/listdiff_op_test.py
x = [1, 2, 3, 4]
y = [1, 2]
out = [3, 4]
idx = [2, 3]
self._testListDiff(x, y, out, idx)
