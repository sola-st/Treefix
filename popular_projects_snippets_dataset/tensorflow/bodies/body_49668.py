# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/utils/metrics_utils.py
"""Decorated function with `add_update()`."""
strategy = distribution_strategy_context.get_strategy()

for weight in metric_obj.weights:
    if (backend.is_tpu_strategy(strategy) and
        not strategy.extended.variable_created_in_scope(weight)
        and not distribution_strategy_context.in_cross_replica_context()):
        raise ValueError(
            'Trying to run metric.update_state in replica context when '
            'the metric was not created in TPUStrategy scope. '
            'Make sure the keras Metric is created in TPUstrategy scope. ')

with tf_utils.graph_context_for_symbolic_tensors(*args, **kwargs):
    update_op = update_state_fn(*args, **kwargs)
if update_op is not None:  # update_op will be None in eager execution.
    metric_obj.add_update(update_op)
exit(update_op)
