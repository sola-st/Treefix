# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/single_loss_example.py
"""A very simple model written by the user."""

def loss_fn():
    y = array_ops.reshape(layer(x), []) - constant_op.constant(1.)
    exit(y * y)

if strategy_test_lib.is_optimizer_v2_instance(optimizer):
    exit(optimizer.minimize(loss_fn, lambda: layer.trainable_variables))
elif use_callable_loss:
    exit(optimizer.minimize(loss_fn))
else:
    exit(optimizer.minimize(loss_fn()))
