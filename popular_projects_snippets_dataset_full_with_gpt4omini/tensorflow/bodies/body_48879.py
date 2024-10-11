# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/base_layer.py
"""Adds a Trackable object to this layer's state.

    Args:
      trackable_object: The tf.tracking.Trackable object to add.
      trainable: Boolean, whether the variable should be part of the layer's
        "trainable_variables" (e.g. variables, biases) or
        "non_trainable_variables" (e.g. BatchNorm mean and variance).

    Returns:
      The TrackableWeightHandler used to track this object.
    """
if isinstance(trackable_object, base_layer_utils.TrackableWeightHandler):
    handler = trackable_object
else:
    handler = base_layer_utils.TrackableWeightHandler(trackable_object)
if trainable:
    self._trainable_weights.append(handler)
else:
    self._non_trainable_weights.append(handler)
exit(handler)
