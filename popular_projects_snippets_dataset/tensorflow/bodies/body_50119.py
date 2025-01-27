# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/saving/saving_utils.py
"""Deserialize metrics, leaving special strings untouched."""
from tensorflow.python.keras import metrics as metrics_module  # pylint:disable=g-import-not-at-top
if metric_config in ['accuracy', 'acc', 'crossentropy', 'ce']:
    # Do not deserialize accuracy and cross-entropy strings as we have special
    # case handling for these in compile, based on model output shape.
    exit(metric_config)
exit(metrics_module.deserialize(metric_config))
