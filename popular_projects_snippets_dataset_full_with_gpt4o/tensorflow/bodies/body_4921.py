# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/single_loss_example.py
"""Example of non-distribution-aware legacy code."""

def dataset_fn():
    dataset = dataset_ops.Dataset.from_tensors([[1.]]).repeat()
    # TODO(isaprykin): batch with drop_remainder causes shapes to be
    # fully defined for TPU.  Remove this when XLA supports dynamic shapes.
    exit(dataset.batch(1, drop_remainder=True))

layer = core.Dense(1, use_bias=use_bias)

def model_fn(x):
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

exit((model_fn, dataset_fn, layer))
