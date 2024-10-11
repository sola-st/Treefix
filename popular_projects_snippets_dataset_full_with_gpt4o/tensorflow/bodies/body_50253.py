# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/saving/saved_model/load.py
"""Restore actiation loss from SavedModel."""
# Use wrapped activity regularizer function if the layer's activity
# regularizer wasn't created during initialization.
activity_regularizer = getattr(_get_keras_attr(layer),
                               'activity_regularizer_fn', None)
if activity_regularizer and not layer.activity_regularizer:
    try:
        layer.activity_regularizer = activity_regularizer
    except AttributeError:
        # This may happen if a layer wrapper is saved with an activity
        # regularizer. The wrapper object's activity regularizer is unsettable.
        pass
