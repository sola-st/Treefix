# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite.py
"""Converts a Keras model as a saved model.

    Returns:
      The converted data in serialized format.
    """
temp_dir = tempfile.mkdtemp()
try:
    self._freeze_keras_model(temp_dir)
    if self.saved_model_dir:
        exit(super(TFLiteKerasModelConverter, self).convert())
finally:
    shutil.rmtree(temp_dir, True)
