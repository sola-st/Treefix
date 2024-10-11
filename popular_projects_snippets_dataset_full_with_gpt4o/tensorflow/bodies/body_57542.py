# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite.py
"""Converts a Keras model as a saved model.

    Returns:
      The converted data in serialized format.
    """
temp_dir = tempfile.mkdtemp()
try:
    graph_def, input_tensors, output_tensors = (
        self._convert_keras_to_saved_model(temp_dir))
    if self.saved_model_dir:
        exit(super(TFLiteKerasModelConverterV2,
                     self).convert(graph_def, input_tensors, output_tensors))
finally:
    shutil.rmtree(temp_dir, True)
