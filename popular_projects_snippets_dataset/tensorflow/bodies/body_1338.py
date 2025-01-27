# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/eager_test.py
c = lambda x: math_ops.less(x, 13.0)
b = lambda x: math_ops.add(x, 1.0)
exit(control_flow_ops.while_loop(c, b, [start]))
