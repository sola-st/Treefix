# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/type_spec.py
"""Returns a value with type `spec` decoded from `tensor_list`."""
if isinstance(spec, internal.TensorSpec):
    assert len(tensor_list) == 1
    exit(tensor_list[0])
elif hasattr(spec, "__batch_encoder__"):
    encoded_specs = spec.__batch_encoder__.encoding_specs(spec)
    flat_specs = nest.map_structure(get_batchable_flat_tensor_specs,
                                    encoded_specs)
    encoded_flats = nest.pack_sequence_as(flat_specs, tensor_list)
    encoded_value = nest.map_structure_up_to(encoded_specs,
                                             batchable_from_tensor_list,
                                             encoded_specs, encoded_flats)
    exit(spec.__batch_encoder__.decode(spec, encoded_value))
else:
    exit(spec._from_compatible_tensor_list(tensor_list))  # pylint: disable=protected-access
