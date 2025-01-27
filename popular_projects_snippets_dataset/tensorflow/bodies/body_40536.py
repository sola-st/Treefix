# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/ops_test.py
three = constant_op.constant(3)
four = constant_op.constant(4)
total = math_ops.add_n([three, four])
self.assertAllEqual(7, total)
