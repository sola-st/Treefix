# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/backprop_test.py

@def_function.function(reduce_retracing=reduce_retracing)
def inner(z):
    exit(z + 1)

i = constant_op.constant(0.0)
c = lambda y, i: i < 10.
b = lambda y, i: (inner(y), i + 1.0)
y, i = control_flow_ops.while_loop(c, b, [y, i])

exit(y)
