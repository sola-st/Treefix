# Extracted from ./data/repos/tensorflow/tensorflow/python/tools/saved_model_cli.py
"""Add parser for `show`."""
show_msg = (
    'Usage examples:\n'
    'To show all tag-sets in a SavedModel:\n'
    '$saved_model_cli show --dir /tmp/saved_model\n\n'
    'To show all available SignatureDef keys in a '
    'MetaGraphDef specified by its tag-set:\n'
    '$saved_model_cli show --dir /tmp/saved_model --tag_set serve\n\n'
    'For a MetaGraphDef with multiple tags in the tag-set, all tags must be '
    'passed in, separated by \';\':\n'
    '$saved_model_cli show --dir /tmp/saved_model --tag_set serve,gpu\n\n'
    'To show all inputs and outputs TensorInfo for a specific'
    ' SignatureDef specified by the SignatureDef key in a'
    ' MetaGraph.\n'
    '$saved_model_cli show --dir /tmp/saved_model --tag_set serve'
    ' --signature_def serving_default\n\n'
    'To show all ops in a MetaGraph.\n'
    '$saved_model_cli show --dir /tmp/saved_model --tag_set serve'
    ' --list_ops\n\n'
    'To show all available information in the SavedModel:\n'
    '$saved_model_cli show --dir /tmp/saved_model --all')
parser_show = subparsers.add_parser(
    'show',
    description=show_msg,
    formatter_class=argparse.RawTextHelpFormatter)
parser_show.set_defaults(func=show)
