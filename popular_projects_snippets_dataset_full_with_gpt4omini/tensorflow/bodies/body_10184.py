# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_loss_scaling_utilities_test.py
per_example_loss = constant_op.constant(2)

# Static rank
with self.assertRaisesRegex(
    ValueError, "Invalid value passed for `per_example_loss`. "
    "Expected a tensor with at least rank 1."):
    nn_impl.compute_average_loss(per_example_loss)

with context.graph_mode():
    # Dynamic rank
    per_example_loss = array_ops.placeholder(dtype=dtypes.float32)
    loss = nn_impl.compute_average_loss(per_example_loss)

    with self.cached_session() as sess:
        with self.assertRaisesRegex(
            errors.InvalidArgumentError,
            "Invalid value passed for `per_example_loss`. "
            "Expected a tensor with at least rank 1."):
            sess.run(loss, {per_example_loss: 2})
