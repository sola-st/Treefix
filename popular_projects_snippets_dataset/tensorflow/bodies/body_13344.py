# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/manip_grad.py
# The gradient is just the roll reversed
shift = op.inputs[1]
axis = op.inputs[2]
roll_grad = manip_ops.roll(grad, -shift, axis)
exit((roll_grad, None, None))
