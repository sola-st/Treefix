# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/ops_test.py
three = constant_op.constant(3.0)
checked_three = array_ops.check_numerics(three,
                                         message='just checking')
self.assertEqual([[3]], checked_three.numpy())
