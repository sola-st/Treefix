# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/tflite_convert.py
"""Returns ArgumentParser for tflite_convert for TensorFlow 2.0.

  Args:
    parser: ArgumentParser
  """
# Input file flags.
input_file_group = parser.add_mutually_exclusive_group()
input_file_group.add_argument(
    "--saved_model_dir",
    type=str,
    help="Full path of the directory containing the SavedModel.")
input_file_group.add_argument(
    "--keras_model_file",
    type=str,
    help="Full filepath of HDF5 file containing tf.Keras model.")
# SavedModel related flags.
parser.add_argument(
    "--saved_model_tag_set",
    type=str,
    help=("Comma-separated set of tags identifying the MetaGraphDef within "
          "the SavedModel to analyze. All tags must be present. In order to "
          "pass in an empty tag set, pass in \"\". (default \"serve\")"))
parser.add_argument(
    "--saved_model_signature_key",
    type=str,
    help=("Key identifying the SignatureDef containing inputs and outputs. "
          "(default DEFAULT_SERVING_SIGNATURE_DEF_KEY)"))

# Enables 1.X converter in 2.X.
parser.add_argument(
    "--enable_v1_converter",
    action="store_true",
    help=("Enables the TensorFlow V1 converter in 2.0"))
