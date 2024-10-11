# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/tflite_convert.py
"""Calls function to convert the TensorFlow 2.0 model into a TFLite model.

  Args:
    flags: argparse.Namespace object.

  Raises:
    ValueError: Unsupported file format.
  """
# Load the model.
if flags.saved_model_dir:
    converter = lite.TFLiteConverterV2.from_saved_model(
        flags.saved_model_dir,
        signature_keys=_parse_array(flags.saved_model_signature_key),
        tags=_parse_set(flags.saved_model_tag_set))
elif flags.keras_model_file:
    model = keras_deps.get_load_model_function()(flags.keras_model_file)
    converter = lite.TFLiteConverterV2.from_keras_model(model)

converter.experimental_new_converter = flags.experimental_new_converter

if flags.experimental_new_quantizer is not None:
    converter.experimental_new_quantizer = flags.experimental_new_quantizer

# Convert the model.
tflite_model = converter.convert()
with open(flags.output_file, "wb") as f:
    f.write(tflite_model)
