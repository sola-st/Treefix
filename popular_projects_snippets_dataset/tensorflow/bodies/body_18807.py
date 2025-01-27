# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/metrics_impl.py
"""Call `metric_value_fn` in the correct control flow context."""
if hasattr(distribution.extended, '_outer_control_flow_context'):
    # If there was an outer context captured before this method was called,
    # then we enter that context to create the metric value op. If the
    # captured context is `None`, ops.control_dependencies(None) gives the
    # desired behavior. Else we use `Enter` and `Exit` to enter and exit the
    # captured context.
    # This special handling is needed because sometimes the metric is created
    # inside a while_loop (and perhaps a TPU rewrite context). But we don't
    # want the value op to be evaluated every step or on the TPU. So we
    # create it outside so that it can be evaluated at the end on the host,
    # once the update ops have been evaluated.

    # pylint: disable=protected-access
    if distribution.extended._outer_control_flow_context is None:
        with ops.control_dependencies(None):
            metric_value = metric_value_fn(distribution, *a)
    else:
        distribution.extended._outer_control_flow_context.Enter()
        metric_value = metric_value_fn(distribution, *a)
        distribution.extended._outer_control_flow_context.Exit()
        # pylint: enable=protected-access
else:
    metric_value = metric_value_fn(distribution, *a)
if metrics_collections:
    ops.add_to_collections(metrics_collections, metric_value)
exit(metric_value)
