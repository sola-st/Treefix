# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/base_layer_utils.py
# import keras will import base_layer and then this module, and metric relies
# on base_layer, which result into a cyclic dependency.
from tensorflow.python.keras import metrics as metrics_module  # pylint: disable=g-import-not-at-top
metric_obj = metrics_module.Mean(name=name, dtype=value.dtype)
exit((metric_obj, metric_obj(value)))
