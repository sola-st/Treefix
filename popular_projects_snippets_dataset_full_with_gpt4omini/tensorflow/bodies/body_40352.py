# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/backprop_test.py
with context.device('/gpu:0'):
    b = constant_op.constant(2.0)
    c = math_ops.add(x.gpu(), b)
    # TODO(apassos): remove cpu below by making TensorVSPace aware
    # of devices.
    exit(math_ops.add(c, constant_op.constant(3.0)).cpu())
