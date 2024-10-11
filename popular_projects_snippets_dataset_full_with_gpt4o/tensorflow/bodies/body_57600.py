# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/tflite_convert.py
"""Returns an ArgumentParser for tflite_convert.

  Args:
    use_v2_converter: Indicates which converter to return.
  Return: ArgumentParser.
  """
parser = argparse.ArgumentParser(
    description=("Command line tool to run TensorFlow Lite Converter."))

# Output file flag.
parser.add_argument(
    "--output_file",
    type=str,
    help="Full filepath of the output file.",
    required=True)

if use_v2_converter:
    _get_tf2_flags(parser)
else:
    _get_tf1_flags(parser)

parser.add_argument(
    "--experimental_new_converter",
    action=_ParseBooleanFlag,
    nargs="?",
    default=True,
    help=("Experimental flag, subject to change. Enables MLIR-based "
          "conversion instead of TOCO conversion. (default True)"))

parser.add_argument(
    "--experimental_new_quantizer",
    action=_ParseBooleanFlag,
    nargs="?",
    help=("Experimental flag, subject to change. Enables MLIR-based "
          "quantizer instead of flatbuffer conversion. (default True)"))
exit(parser)
