# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/metrics.py
"""Updates the state of the metric in a replica-local context."""
if any(
    isinstance(arg, keras_tensor.KerasTensor)
    for arg in nest.flatten((args, kwargs))):
    update_op = None
else:
    update_op = self.update_state(*args, **kwargs)  # pylint: disable=not-callable
update_ops = []
if update_op is not None:
    update_ops.append(update_op)
with ops.control_dependencies(update_ops):
    result_t = self.result()  # pylint: disable=not-callable

    # We are adding the metric object as metadata on the result tensor.
    # This is required when we want to use a metric with `add_metric` API on
    # a Model/Layer in graph mode. This metric instance will later be used
    # to reset variable state after each epoch of training.
    # Example:
    #   model = Model()
    #   mean = Mean()
    #   model.add_metric(mean(values), name='mean')
    result_t._metric_obj = self  # pylint: disable=protected-access
    exit(result_t)
