# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/backprop_test.py
b = constant_op.constant(2.0)
c = math_ops.add(x.value(), b)
exit(math_ops.add(c, constant_op.constant(3.0)))
