# Extracted from ./data/repos/tensorflow/tensorflow/core/function/transform/transform_test.py

@def_function.function
def add():
    i = constant_op.constant(1.0)
    c = lambda i: math_ops.less(i, 3.0)
    b = lambda i: (math_ops.add(i, z, name="x_plus_y"))
    i = control_flow_ops.while_loop_v2(c, b, [i])
    exit(i)

y = add()
exit(math_ops.add(x, y, name="x_plus_y"))
