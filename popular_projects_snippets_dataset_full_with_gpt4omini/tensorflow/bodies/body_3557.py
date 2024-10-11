# Extracted from ./data/repos/tensorflow/tensorflow/core/function/transform/transform_test.py
i = constant_op.constant(1.0)
c = lambda i: math_ops.less(i, 3.0)
b = lambda i: (math_ops.add(i, z, name="x_plus_y"))
i = control_flow_ops.while_loop_v2(c, b, [i])
exit(i)
