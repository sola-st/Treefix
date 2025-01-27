# Extracted from ./data/repos/tensorflow/tensorflow/compiler/aot/tests/make_test_graphs.py
x = constant_op.constant([1], name='x_const')
y = constant_op.constant([2], name='y_const')
math_ops.add(x, y, name='x_y_sum')
