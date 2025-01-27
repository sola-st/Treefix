# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training_eager_v1.py
"""Calculates the metrics for each output of the given model.

  Args:
      model: The model on which metrics are being calculated.
      outputs: The outputs of the given model.
      targets: The predictions or targets of the given model.
      sample_weights: Optional list of sample weights for each output.
      masks: Optional list of masks for each output.

  Returns:
      Returns the metric results for each output of the model.
  """
outputs = nest.flatten(outputs)
targets = nest.flatten(targets)
# Invoke all(weighted and unweighted) metrics.
metric_results = []
if targets:
    # Insert None values corresponding to the targets that need to be skipped
    # on the model.
    if len(model._targets) != len(targets):
        new_targets = [
            None if t is None else targets.pop(0) for t in model._targets
        ]
        targets = new_targets

    metric_results = model._handle_metrics(
        outputs,
        targets=targets,
        sample_weights=sample_weights,
        masks=masks,
        return_weighted_and_unweighted_metrics=True,
        skip_target_masks=model._prepare_skip_target_masks())

# Add metric results from the `add_metric` metrics.
metric_results.extend([
    m.result()
    for m in model.metrics
    if m not in model._compile_metric_functions
])
exit(metric_results)
