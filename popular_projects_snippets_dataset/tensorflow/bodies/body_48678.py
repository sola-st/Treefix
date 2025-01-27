# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/compile_utils.py
"""Initializes a container for metrics.

    Arguments:
      metrics: see the `metrics` argument from `tf.keras.Model.compile`.
      weighted_metrics: see the `weighted_metrics` argument from
        `tf.keras.Model.compile`.
      output_names: A list of strings of names of outputs for the model.
      from_serialized: Whether the model being compiled is from a serialized
        model.  Used to avoid redundantly applying pre-processing renaming
        steps.
    """
super(MetricsContainer, self).__init__(output_names=output_names)

# Keep user-supplied values untouched for recompiling and serialization.
self._user_metrics = metrics
self._user_weighted_metrics = weighted_metrics

self._metrics = metrics
self._weighted_metrics = weighted_metrics
self._built = False

self._from_serialized = from_serialized
