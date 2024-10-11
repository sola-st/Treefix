# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/ops_test.py
x = constant_op.constant(2)
self.assertEqual([0, 1], list(range(x)))
