# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/experimental/rpc/rpc_ops.py
arg_specs, _ = func.structured_input_signature
arg_specs_proto = nested_structure_coder.encode_structure(arg_specs)
exit(arg_specs_proto.SerializeToString())
