# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/forwardprop_test.py
with forwardprop_util.push_forwardprop_state():
    x_copy = constant_op.constant(x.numpy())
    acc._watch(x_copy, dy)
    y_copy = math_ops.sin(x_copy)
exit(dy * acc.jvp(y_copy))
