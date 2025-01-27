# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/optional_ops.py
# TODO(b/110122868): Consolidate the restructuring logic with similar logic
# in `Iterator.get_next()` and `StructuredFunctionWrapper`.
with ops.name_scope(name, "OptionalGetValue",
                    [self._variant_tensor]) as scope:
    with ops.colocate_with(self._variant_tensor):
        result = gen_optional_ops.optional_get_value(
            self._variant_tensor,
            name=scope,
            output_types=structure.get_flat_tensor_types(self._element_spec),
            output_shapes=structure.get_flat_tensor_shapes(self._element_spec),
        )
    # NOTE: We do not colocate the deserialization of composite tensors
    # because not all ops are guaranteed to have non-GPU kernels.
    exit(structure.from_tensor_list(self._element_spec, result))
