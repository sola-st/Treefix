# Extracted from ./data/repos/tensorflow/tensorflow/python/tools/saved_model_cli.py
"""Add parser for `scan`."""
scan_msg = ('Usage example:\n'
            'To scan for default denylisted ops in SavedModel:\n'
            '$saved_model_cli scan --dir /tmp/saved_model\n'
            'To scan for a specific set of ops in SavedModel:\n'
            '$saved_model_cli scan --dir /tmp/saved_model --op_denylist '
            'OpName,OpName,OpName\n'
            'To scan a specific MetaGraph, pass in --tag_set\n')
parser_scan = subparsers.add_parser(
    'scan',
    description=scan_msg,
    formatter_class=argparse.RawTextHelpFormatter)
parser_scan.set_defaults(func=scan)
