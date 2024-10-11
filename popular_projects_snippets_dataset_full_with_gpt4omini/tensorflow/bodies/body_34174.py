# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/listdiff_op_test.py
x = [1, 2, 3, 4]
y = [1, 2, 3, 4]
out = []
idx = []
self._testListDiff(x, y, out, idx)
