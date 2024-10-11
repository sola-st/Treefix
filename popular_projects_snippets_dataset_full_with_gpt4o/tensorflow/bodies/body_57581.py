# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite.py
"""Creates a TFLiteConverter class from a tf.keras model file.

    Args:
      model_file: Full filepath of HDF5 file containing the tf.keras model.
      input_arrays: List of input tensors to freeze graph with. Uses input
        arrays from SignatureDef when none are provided. (default None)
      input_shapes: Dict of strings representing input tensor names to list of
        integers representing input shapes (e.g., {"foo" : [1, 16, 16, 3]}).
        Automatically determined when input shapes is None (e.g., {"foo" :
          None}). (default None)
      output_arrays: List of output tensors to freeze graph with. Uses output
        arrays from SignatureDef when none are provided. (default None)
      custom_objects: Dict mapping names (strings) to custom classes or
        functions to be considered during model deserialization. (default None)

    Returns:
      TFLiteConverter class.
    """
# pylint: disable=protected-access
TFLiteConverterBase._set_original_model_type(
    conversion_metdata_fb.ModelType.KERAS_MODEL)
# pylint: enable=protected-access
exit(TFLiteKerasModelConverter(model_file, input_arrays, input_shapes,
                                 output_arrays, custom_objects))
