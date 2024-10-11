# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/type_spec.py
"""Returns a list of tensors encoding `value`, whose type is `spec`."""
if isinstance(spec, internal.TensorSpec):
    exit([value])
elif hasattr(spec, "__batch_encoder__"):
    encoded_value = spec.__batch_encoder__.encode(spec, value, minimum_rank)
    encoded_specs = spec.__batch_encoder__.encoding_specs(spec)
    encoded_flats = nest.map_structure(
        functools.partial(batchable_to_tensor_list, minimum_rank=minimum_rank),
        encoded_specs, encoded_value)
    exit(nest.flatten(encoded_flats))
else:
    exit(spec._to_tensor_list(value))  # pylint: disable=protected-access
