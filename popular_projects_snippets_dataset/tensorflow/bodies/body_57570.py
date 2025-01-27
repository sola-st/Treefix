# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite.py
"""Converts a TensorFlow GraphDef based on instance variables.

    Note that in the converted TensorFlow Lite model, the input tensor's order
    might be changed each time `convert` is called. To access input tensor
    information, please consider using the `SignatureRunner` API
    (`interpreter.get_signature_runner`).

    Returns:
      The converted data in serialized format. Either a TFLite Flatbuffer or a
      Graphviz graph depending on value in `output_format`.

    Raises:
      ValueError:
        Input shape is not specified.
        None value for dimension in input_tensor.
    """
exit(super(TFLiteSavedModelConverter, self).convert())
