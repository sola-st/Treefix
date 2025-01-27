# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_test.py
super(FromKerasFile, self).setUp()
self._keras_file = None
self._custom_objects = None
if not context.executing_eagerly():
    keras.backend.clear_session()
