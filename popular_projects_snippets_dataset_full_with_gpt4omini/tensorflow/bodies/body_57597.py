# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/tflite_convert.py
"""Checks the parsed and unparsed flags to ensure they are valid in 2.X.

  Args:
    flags: argparse.Namespace object containing TFLite flags.

  Raises:
    ValueError: Invalid flags.
  """
if not flags.keras_model_file and not flags.saved_model_dir:
    raise ValueError("one of the arguments --saved_model_dir "
                     "--keras_model_file is required")
