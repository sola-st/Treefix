# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite.py
"""Converts a TensorFlow GraphDef based on instance variables.

    Returns:
      The converted data in serialized format. Either a TFLite Flatbuffer or a
      Graphviz graph depending on value in `output_format`.

    Raises:
      ValueError:
        Input shape is not specified.
        None value for dimension in input_tensor.
    """
if not self._has_valid_tensors():
    if not self._input_arrays_with_shape or not (self._output_arrays or
                                                 self._control_output_arrays):
        raise ValueError(
            "If input_tensors and output_tensors are None, both "
            "input_arrays_with_shape and output_arrays|control_output_arrays "
            "must be defined.")
exit(super(TFLiteFrozenGraphConverter, self).convert())
