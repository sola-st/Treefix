# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training_v1.py
"""Handles calling metric functions.

    Args:
      outputs: List of outputs (predictions).
      targets: List of targets.
      skip_target_masks: Optional. List of boolean for whether the corresponding
        target should be ignored or not.
      sample_weights: Optional list of sample weight arrays.
      masks: List of computed output mask values.
      return_weighted_metrics: Flag that indicates whether weighted metrics
        should be computed instead of unweighted metrics. This flag is ignored
        when `return_weighted_and_unweighted_metrics` is enabled.
      return_weighted_and_unweighted_metrics: Flag that is used to indicate
        whether both weighted and unweighted metrics should be computed. When
        this is not enabled, we use `return_weighted_metrics` param to indicate
        whether weighted or unweighted metrics should be returned.

    Returns:
      A list of metric result tensors.
    """
# TODO(scottzhu): Update this to use the new training_endpoints. Currently
# the eager and graph logic is bit different.
skip_target_masks = skip_target_masks or [False] * len(outputs)
metric_results = []
with backend.name_scope('metrics'):
    # Invoke all metrics added using `compile`.
    for i in range(len(outputs)):
        if skip_target_masks[i]:
            continue
        output = outputs[i] if outputs else None
        target = targets[i] if targets else None
        output_mask = masks[i] if masks else None

        if (return_weighted_and_unweighted_metrics or
            not return_weighted_metrics):
            metric_results.extend(
                self._handle_per_output_metrics(self._per_output_metrics[i],
                                                target, output, output_mask))
        if return_weighted_and_unweighted_metrics or return_weighted_metrics:
            metric_results.extend(
                self._handle_per_output_metrics(
                    self._per_output_weighted_metrics[i],
                    target,
                    output,
                    output_mask,
                    weights=sample_weights[i] if sample_weights else None))
exit(metric_results)
