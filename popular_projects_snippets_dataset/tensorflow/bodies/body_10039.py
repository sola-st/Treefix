# Extracted from ./data/repos/tensorflow/tensorflow/python/tools/saved_model_cli.py
"""Add parser for `freeze_model`."""
compile_msg = '\n'.join(
    ['Usage example:',
     'To freeze a SavedModel in preparation for tfcompile:',
     '$saved_model_cli freeze_model \\',
     '   --dir /tmp/saved_model \\',
     '   --tag_set serve \\',
     '   --output_prefix /tmp/saved_model_xla_aot',
    ])

parser_compile = subparsers.add_parser(
    'freeze_model',
    description=compile_msg,
    formatter_class=argparse.RawTextHelpFormatter)
parser_compile.set_defaults(func=freeze_model)
