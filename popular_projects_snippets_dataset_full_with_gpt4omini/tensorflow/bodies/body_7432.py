# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/experimental/rpc/rpc_ops.py
if args is None:
    args = []
if input_specs:
    nest.assert_same_structure(args, input_specs)
flat_inputs = nest.flatten(args)
exit(flat_inputs)
