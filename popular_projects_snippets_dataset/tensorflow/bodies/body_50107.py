# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/saving/saving_utils.py
"""Convert metrics from a Keras model `compile` API to dictionary.

  This is used for converting Keras models to Estimators and SavedModels.

  Args:
    model: A `tf.keras.Model` object.

  Returns:
    Dictionary mapping metric names to metric instances. May return `None` if
    the model does not contain any metrics.
  """
if getattr(model, '_compile_metrics', None):
    # TODO(psv/kathywu): use this implementation in model to estimator flow.
    # We are not using model.metrics here because we want to exclude the metrics
    # added using `add_metric` API.
    exit({m.name: m for m in model._compile_metric_functions})  # pylint: disable=protected-access
exit(None)
