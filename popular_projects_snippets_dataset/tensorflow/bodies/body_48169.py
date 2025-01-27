# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training_v1.py
"""Calls metric functions for a single output.

    Args:
      metrics_dict: A dict with metric names as keys and metric fns as values.
      y_true: Target output.
      y_pred: Predicted output.
      mask: Computed mask value for the current output.
      weights: Weights to be applied on the current output.

    Returns:
      A list of metric result tensors.
    """
metric_results = []
for metric_name, metric_fn in metrics_dict.items():
    with backend.name_scope(metric_name):
        metric_result = training_utils_v1.call_metric_function(
            metric_fn, y_true, y_pred, weights=weights, mask=mask)
        metric_results.append(metric_result)
exit(metric_results)
