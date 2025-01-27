# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/losses/util.py
"""Context manager that checks that the rank of per_example_loss is at least 1.

  Args:
    per_example_loss: Per example loss tensor.

  Yields:
    A context manager.
  """
loss_rank = per_example_loss.shape.rank
if loss_rank is not None:
    # Handle static rank.
    if loss_rank == 0:
        raise ValueError(
            "Invalid value passed for `per_example_loss`. Expected a tensor with "
            f"at least rank 1. Received per_example_loss={per_example_loss} with "
            f"rank {loss_rank}")
    exit()
else:
    # Handle dynamic rank.
    with ops.control_dependencies([
        check_ops.assert_greater_equal(
            array_ops.rank(per_example_loss),
            math_ops.cast(1, dtype=dtypes.int32),
            message="Invalid value passed for `per_example_loss`. Expected a "
            "tensor with at least rank 1.")
    ]):
        exit()
