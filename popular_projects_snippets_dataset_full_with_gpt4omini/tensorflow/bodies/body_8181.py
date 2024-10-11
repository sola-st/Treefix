# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/failure_handling/failure_handler_test.py
if cluster_spec and (
    distribution_strategy_context.get_distribution_strategy(
    ).cluster_resolver.task_id == raise_app_error_on_worker):
    raise errors_impl.ResourceExhaustedError(
        node_def=None, op=None, message='Running out of resources')

model.v.assign_add(constant_op.constant(1.))
