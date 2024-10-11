# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/tflite_convert.py
"""Makes a TFLiteConverter object based on the flags provided.

  Args:
    flags: argparse.Namespace object containing TFLite flags.

  Returns:
    TFLiteConverter object.

  Raises:
    ValueError: Invalid flags.
  """
# Parse input and output arrays.
input_arrays = _parse_array(flags.input_arrays)
input_shapes = None
if flags.input_shapes:
    input_shapes_list = [
        _parse_array(shape, type_fn=int)
        for shape in flags.input_shapes.split(":")
    ]
    input_shapes = dict(list(zip(input_arrays, input_shapes_list)))
output_arrays = _parse_array(flags.output_arrays)

converter_kwargs = {
    "input_arrays": input_arrays,
    "input_shapes": input_shapes,
    "output_arrays": output_arrays
}

# Create TFLiteConverter.
if flags.graph_def_file:
    converter_fn = lite.TFLiteConverter.from_frozen_graph
    converter_kwargs["graph_def_file"] = flags.graph_def_file
elif flags.saved_model_dir:
    converter_fn = lite.TFLiteConverter.from_saved_model
    converter_kwargs["saved_model_dir"] = flags.saved_model_dir
    converter_kwargs["tag_set"] = _parse_set(flags.saved_model_tag_set)
    converter_kwargs["signature_key"] = flags.saved_model_signature_key
elif flags.keras_model_file:
    converter_fn = lite.TFLiteConverter.from_keras_model_file
    converter_kwargs["model_file"] = flags.keras_model_file
else:
    raise ValueError("--graph_def_file, --saved_model_dir, or "
                     "--keras_model_file must be specified.")

exit(converter_fn(**converter_kwargs))
