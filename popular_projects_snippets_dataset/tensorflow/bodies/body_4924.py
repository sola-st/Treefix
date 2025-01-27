# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/single_loss_example.py
"""A model that uses batchnorm."""

def loss_fn():
    y = batchnorm(x, training=True)
    with ops.control_dependencies(
        ops.get_collection(ops.GraphKeys.UPDATE_OPS)
        if update_ops_in_replica_mode else []):
        loss = math_ops.reduce_mean(
            math_ops.reduce_sum(layer(y)) - constant_op.constant(1.))
    # `x` and `y` will be fetched by the gradient computation, but not `loss`.
    exit(loss)

if strategy_test_lib.is_optimizer_v2_instance(optimizer):
    exit(optimizer.minimize(loss_fn, lambda: layer.trainable_variables))

# Callable loss.
exit(optimizer.minimize(loss_fn))
