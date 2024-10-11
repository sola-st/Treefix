# Extracted from ./data/repos/tensorflow/tensorflow/lite/toco/python/toco_from_protos.py
global FLAGS
parser = argparse.ArgumentParser(
    description="Invoke toco using protos as input.")
parser.add_argument(
    "model_proto_file",
    type=str,
    help="File containing serialized proto that describes the model.")
parser.add_argument(
    "toco_proto_file",
    type=str,
    help="File containing serialized proto describing how TOCO should run.")
parser.add_argument(
    "model_input_file", type=str, help="Input model is read from this file.")
parser.add_argument(
    "model_output_file",
    type=str,
    help="Result of applying TOCO conversion is written here.")
parser.add_argument(
    "--debug_proto_file",
    type=str,
    default="",
    help=("File containing serialized `GraphDebugInfo` proto that describes "
          "logging information."))
parser.add_argument(
    "--enable_mlir_converter",
    action="store_true",
    help=("Boolean indicating whether to enable MLIR-based conversion "
          "instead of TOCO conversion. (default False)"))

FLAGS, unparsed = parser.parse_known_args()

app.run(main=execute, argv=[sys.argv[0]] + unparsed)
