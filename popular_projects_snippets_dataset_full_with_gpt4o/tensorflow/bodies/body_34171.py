# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/listdiff_op_test.py
x = [1, 4, 3, 2]
y = [4, 2]
out = [1, 3]
idx = [0, 2]
self._testListDiff(x, y, out, idx)
