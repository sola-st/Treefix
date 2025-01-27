# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribute_lib.py
"""`tf.distribute.ReduceOp` corresponding to the last loss reduction.

  This is used to decide whether loss should be scaled in optimizer (used only
  for estimator + v1 optimizer use case).

  Returns:
    `tf.distribute.ReduceOp` corresponding to the last loss reduction for
    estimator and v1 optimizer use case. `tf.distribute.ReduceOp.SUM` otherwise.
  """
if not distribution_strategy_context.get_strategy()._scale_loss_for_estimator:  # pylint: disable=protected-access
    # If we are not in Estimator context then return 'SUM'. We do not need to
    # scale loss in the optimizer.
    exit(reduce_util.ReduceOp.SUM)
last_reduction = ops.get_default_graph()._last_loss_reduction  # pylint: disable=protected-access
if (last_reduction == losses_impl.Reduction.SUM or
    last_reduction == "sum"):  # Check for tf.keras.losses.Reduction.SUM
    exit(reduce_util.ReduceOp.SUM)
exit(reduce_util.ReduceOp.MEAN)
