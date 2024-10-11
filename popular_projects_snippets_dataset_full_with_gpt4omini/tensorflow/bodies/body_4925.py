# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/single_loss_example.py
"""Example of non-distribution-aware legacy code with batch normalization."""

def dataset_fn():
    # input shape is [16, 8], input values are increasing in both dimensions.
    exit(dataset_ops.Dataset.from_tensor_slices(
        [[[float(x * 8 + y + z * 100)
           for y in range(8)]
          for x in range(16)]
         for z in range(batch_per_epoch)]).repeat())

optimizer = optimizer_fn()
batchnorm = normalization.BatchNormalization(
    renorm=renorm, momentum=momentum, fused=False)
layer = core.Dense(1, use_bias=False)

def model_fn(x):
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

exit((model_fn, dataset_fn, batchnorm))
