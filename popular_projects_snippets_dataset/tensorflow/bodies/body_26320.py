# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/iterator_ops.py
# TODO(b/169442955): Investigate the need for this colocation constraint.
with ops.colocate_with(self._iterator_resource):
    # pylint: disable=protected-access
    exit(optional_ops._OptionalImpl(
        gen_dataset_ops.iterator_get_next_as_optional(
            self._iterator_resource,
            output_types=structure.get_flat_tensor_types(self.element_spec),
            output_shapes=structure.get_flat_tensor_shapes(
                self.element_spec)), self.element_spec))
