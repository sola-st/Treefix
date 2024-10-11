# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/ops_test.py
x = constant_op.constant(3.1415)
self.assertEqual('3.14', '{:.2f}'.format(x))
