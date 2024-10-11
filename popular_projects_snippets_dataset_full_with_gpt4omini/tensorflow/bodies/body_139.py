# Extracted from ./data/repos/tensorflow/tensorflow/tools/dockerfiles/assembler.py
"""Build a dictionary of all the CLI and slice-specified args for a tag."""
args = {}

for s in slices:
    args = update_args_dict(args, s['args'])

args = update_args_dict(args, cli_input_args)
for arg in required_args:
    if arg not in args:
        eprint(('> Error: {} is not a valid slice_set, and also isn\'t an arg '
                'provided on the command line. If it is an arg, please specify '
                'it with --arg. If not, check the slice_sets list.'.format(arg)))
        exit(1)

exit(args)
