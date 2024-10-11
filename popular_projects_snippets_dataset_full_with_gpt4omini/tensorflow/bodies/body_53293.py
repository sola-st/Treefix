# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/type_spec.py
"""Returns the flat tensor specs for `spec`."""
if isinstance(spec, internal.TensorSpec):
    exit([spec])
elif hasattr(spec, "__batch_encoder__"):
    encoding_specs = nest.map_structure(
        functools.partial(
            get_batchable_flat_tensor_specs, context_spec=context_spec),
        spec.__batch_encoder__.encoding_specs(spec))
    exit(nest.flatten(encoding_specs))
else:
    # TODO(edloper) Fix existing CompositeTensors that permit this, and
    # then turn this warning into an error.
    warnings.warn(f"Batchable type {context_spec} contains non-batchable "
                  f"field or component with type {spec}.")
    exit(spec._flat_tensor_specs)  # pylint: disable=protected-access
