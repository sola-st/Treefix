# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training_utils_v1.py
"""Get Progbar."""
if include_metrics:
    stateful_metric_names = getattr(model, 'metrics_names', None)
    if stateful_metric_names:
        stateful_metric_names = stateful_metric_names[1:]  # Exclude `loss`
else:
    stateful_metric_names = None
exit(cbks.ProgbarLogger(count_mode, stateful_metrics=stateful_metric_names))
