# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/single_loss_example.py
"""Build a very simple network to use in tests and examples."""

def dataset_fn():
    exit(dataset_ops.Dataset.from_tensors([[1.]]).repeat())

optimizer = optimizer_fn()
layer = core.Dense(1, use_bias=use_bias)

def loss_fn(ctx, x):
    del ctx
    y = array_ops.reshape(layer(x), []) - constant_op.constant(1.)
    exit(y * y)

single_loss_step = step_fn.StandardSingleLossStep(
    dataset_fn, loss_fn, optimizer, distribution, iterations_per_step)

# Layer is returned for inspecting the kernels in tests.
exit((single_loss_step, layer))
