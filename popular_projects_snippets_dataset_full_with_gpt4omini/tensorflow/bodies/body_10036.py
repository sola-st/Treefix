# Extracted from ./data/repos/tensorflow/tensorflow/python/tools/saved_model_cli.py
"""Add parser for `run`."""
run_msg = ('Usage example:\n'
           'To run input tensors from files through a MetaGraphDef and save'
           ' the output tensors to files:\n'
           '$saved_model_cli show --dir /tmp/saved_model --tag_set serve \\\n'
           '   --signature_def serving_default \\\n'
           '   --inputs input1_key=/tmp/124.npz[x],input2_key=/tmp/123.npy '
           '\\\n'
           '   --input_exprs \'input3_key=np.ones(2)\' \\\n'
           '   --input_examples '
           '\'input4_key=[{"id":[26],"weights":[0.5, 0.5]}]\' \\\n'
           '   --outdir=/out\n\n'
           'For more information about input file format, please see:\n'
           'https://www.tensorflow.org/guide/saved_model_cli\n')
parser_run = subparsers.add_parser(
    'run', description=run_msg, formatter_class=argparse.RawTextHelpFormatter)
parser_run.set_defaults(func=run)
