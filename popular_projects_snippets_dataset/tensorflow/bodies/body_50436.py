# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/callbacks.py
"""Computes logs for sending to `on_batch_end` methods."""
metric_names = model.metrics_names
if mode in {ModeKeys.TRAIN, ModeKeys.TEST} and metric_names:
    for label, output in zip(metric_names, outputs):
        logs[prefix + label] = output
else:
    logs['outputs'] = outputs
exit(logs)
