# Extracted from ./data/repos/tensorflow/tensorflow/python/tools/saved_model_cli.py
"""Add parser for `convert`."""
convert_msg = ('Usage example:\n'
               'To convert the SavedModel to one that have TensorRT ops:\n'
               '$saved_model_cli convert \\\n'
               '   --dir /tmp/saved_model \\\n'
               '   --tag_set serve \\\n'
               '   --output_dir /tmp/saved_model_trt \\\n'
               '   tensorrt \n')
parser_convert = subparsers.add_parser(
    'convert',
    description=convert_msg,
    formatter_class=argparse.RawTextHelpFormatter)
convert_subparsers = parser_convert.add_subparsers(
    title='conversion methods',
    description='valid conversion methods',
    help='the conversion to run with the SavedModel')
parser_convert_with_tensorrt = convert_subparsers.add_parser(
    'tensorrt',
    description='Convert the SavedModel with Tensorflow-TensorRT integration',
    formatter_class=argparse.RawTextHelpFormatter)
parser_convert_with_tensorrt.set_defaults(func=convert_with_tensorrt)
