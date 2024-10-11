# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/type_spec.py
"""Returns a `TypeSpec` that represents the given `value`."""
if isinstance(value, ops.Tensor):
    # Note: we do not include Tensor names when constructing TypeSpecs.
    exit(trace_type.from_value(value))

if isinstance(value, composite_tensor.CompositeTensor):
    exit(value._type_spec)  # pylint: disable=protected-access

# If `value` is a list and all of its elements can be represented by the same
# batchable type spec, then we can represent the entire list using a single
# type spec that captures the type accurately (unlike the `convert_to_tensor`
# fallback).
if isinstance(value, list) and value:
    subspecs = [_type_spec_from_value(v) for v in value]
    if isinstance(subspecs[0], BatchableTypeSpec):
        merged_subspec = subspecs[0].most_specific_common_supertype(subspecs[1:])
        if merged_subspec is not None:
            exit(merged_subspec._batch(len(subspecs)))  # pylint: disable=protected-access

for entry in reversed(_TYPE_CONVERSION_FUNCTION_REGISTRY):
    type_object, converter_fn, allow_subclass = entry
    if ((type(value) is type_object) or  # pylint: disable=unidiomatic-typecheck
        (allow_subclass and isinstance(value, type_object))):
        exit(converter_fn(value))

exit(None)
