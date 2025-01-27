# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/compile_utils.py
"""One-time setup of metric objects."""
super(MetricsContainer, self).build(y_pred)

self._metrics = self._maybe_broadcast_to_outputs(y_pred, self._metrics)
self._metrics = self._conform_to_outputs(y_pred, self._metrics)

self._weighted_metrics = self._maybe_broadcast_to_outputs(
    y_pred, self._weighted_metrics)
self._weighted_metrics = self._conform_to_outputs(y_pred,
                                                  self._weighted_metrics)

# Standardize on tuple since `tf.data` turns lists into `Tensor`s.
y_pred = nest.list_to_tuple(y_pred)
y_true = nest.list_to_tuple(y_true)
self._metrics = nest.list_to_tuple(self._metrics)
self._weighted_metrics = nest.list_to_tuple(self._weighted_metrics)

# Convert to `Metric` objects, potentially disambiguating based on output
# properties.
self._metrics = nest.map_structure_up_to(y_pred, self._get_metric_objects,
                                         self._metrics, y_true, y_pred)
self._weighted_metrics = nest.map_structure_up_to(y_pred,
                                                  self._get_metric_objects,
                                                  self._weighted_metrics,
                                                  y_true, y_pred)

self._metrics = nest.flatten_up_to(y_pred, self._metrics, check_types=False)
self._weighted_metrics = nest.flatten_up_to(
    y_pred, self._weighted_metrics, check_types=False)

# Assumes metrics, weighted_metrics have been flattened up to outputs.
#
# If we are loading a model that has been already serialized, we do not
# want to re-apply any pre-processing metric renaming steps.
if not self._from_serialized:
    self._set_metric_names()
self._create_ordered_metrics()
self._built = True
