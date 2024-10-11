# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/experimental/rpc/rpc_ops.py
output_specs = nest.map_structure(type_spec.type_spec_from_value,
                                  func.structured_outputs)
output_specs_proto = nested_structure_coder.encode_structure(output_specs)
exit(output_specs_proto.SerializeToString())
