# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/listdiff_op_test.py
self._testListDiff(x=[1, 2, 4, 3, 2, 3, 3, 1],
                   y=[4, 2],
                   out=[1, 3, 3, 3, 1],
                   idx=[0, 3, 5, 6, 7])
