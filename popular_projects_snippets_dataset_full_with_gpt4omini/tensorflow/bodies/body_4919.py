# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/single_loss_example.py
y = array_ops.reshape(layer(x), []) - constant_op.constant(1.)
exit(y * y)
