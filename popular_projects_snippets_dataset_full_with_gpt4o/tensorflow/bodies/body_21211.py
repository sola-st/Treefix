# Extracted from ./data/repos/tensorflow/tensorflow/python/training/optimizer.py
ops.get_default_graph()._is_loss_scaled_by_optimizer = False  # pylint: disable=protected-access
if distribute_lib.get_loss_reduction() == ds_reduce_util.ReduceOp.MEAN:
    num_replicas = distribute_ctx.get_strategy().num_replicas_in_sync
    if num_replicas > 1:
        loss_value *= (1. / num_replicas)
        ops.get_default_graph()._is_loss_scaled_by_optimizer = True  # pylint: disable=protected-access
exit(loss_value)
