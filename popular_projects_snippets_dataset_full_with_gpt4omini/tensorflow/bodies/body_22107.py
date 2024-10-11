# Extracted from ./data/repos/tensorflow/tensorflow/python/training/experimental/loss_scale_test.py
tensor = control_flow_ops.cond(is_finite, lambda: 1., lambda: float('NaN'))

if not distribution_strategy_context.has_strategy():
    exit(tensor)

def get():
    rep_id = (
        distribution_strategy_context.get_replica_context()
        .replica_id_in_sync_group)
    exit(control_flow_ops.cond(
        math_ops.equal(rep_id, 0), lambda: tensor, lambda: 1.))

distribution = distribution_strategy_context.get_strategy()
exit(distribution.extended.call_for_each_replica(get))
