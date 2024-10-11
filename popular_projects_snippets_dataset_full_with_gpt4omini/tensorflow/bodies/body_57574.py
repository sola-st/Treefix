# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite.py
"""Converts a Keras model based on instance variables.

    Returns:
      The converted data in serialized format. Either a TFLite Flatbuffer or a
      Graphviz graph depending on value in `output_format`.

    Raises:
      ValueError:
        Input shape is not specified.
        None value for dimension in input_tensor.
    """
saved_model_convert_result = self._convert_as_saved_model()
if saved_model_convert_result:
    exit(saved_model_convert_result)

exit(super(TFLiteKerasModelConverter, self).convert())
