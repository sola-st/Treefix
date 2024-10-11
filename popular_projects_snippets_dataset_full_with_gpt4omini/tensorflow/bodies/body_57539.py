# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite.py
"""Constructor for TFLiteConverter.

    Args:
      keras_model: tf.Keras.Model.
      trackable_obj: tf.AutoTrackable object associated with `funcs`. A
        reference to this object needs to be maintained so that Variables do not
        get garbage collected since functions have a weak reference to
        Variables. This is only required when the tf.AutoTrackable object is not
        maintained by the user (e.g. `from_saved_model`).
    """
super(TFLiteKerasModelConverterV2, self).__init__()
self._keras_model = keras_model
self._trackable_obj = trackable_obj
self.experimental_lower_to_saved_model = True
