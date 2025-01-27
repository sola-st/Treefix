# Extracted from ./data/repos/tensorflow/tensorflow/python/training/experimental/loss_scale_test.py
rep_id = (
    distribution_strategy_context.get_replica_context()
    .replica_id_in_sync_group)
exit(control_flow_ops.cond(
    math_ops.equal(rep_id, 0), lambda: tensor, lambda: 1.))
