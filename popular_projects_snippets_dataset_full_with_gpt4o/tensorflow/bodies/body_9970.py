# Extracted from ./data/repos/tensorflow/tensorflow/python/tools/optimize_for_inference.py
"""Parses command line arguments."""
parser = argparse.ArgumentParser()
parser.register("type", "bool", lambda v: v.lower() == "true")
parser.add_argument(
    "--input",
    type=str,
    default="",
    help="TensorFlow \'GraphDef\' file to load.")
parser.add_argument(
    "--output",
    type=str,
    default="",
    help="File to save the output graph to.")
parser.add_argument(
    "--input_names",
    type=str,
    default="",
    help="Input node names, comma separated.")
parser.add_argument(
    "--output_names",
    type=str,
    default="",
    help="Output node names, comma separated.")
parser.add_argument(
    "--frozen_graph",
    nargs="?",
    const=True,
    type="bool",
    default=True,
    help="""\
      If true, the input graph is a binary frozen GraphDef
      file; if false, it is a text GraphDef proto file.\
      """)
parser.add_argument(
    "--placeholder_type_enum",
    type=str,
    default=str(dtypes.float32.as_datatype_enum),
    help="""\
      The AttrValue enum to use for placeholders.
      Or a comma separated list, one value for each placeholder.\
      """)
parser.add_argument(
    "--toco_compatible",
    type=bool,
    default=False,
    help="""\
      If true, only use ops compatible with Tensorflow
      Lite Optimizing Converter.\
      """)
exit(parser.parse_known_args())
