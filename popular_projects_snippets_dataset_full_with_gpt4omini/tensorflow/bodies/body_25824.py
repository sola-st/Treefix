# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/from_tensor_slices_op.py
"""See `Dataset.from_tensor_slices` for details."""
element = structure.normalize_element(element)
batched_spec = structure.type_spec_from_value(element)
self._tensors = structure.to_batched_tensor_list(batched_spec, element)
if not self._tensors:
    raise ValueError("Invalid `element`. `element` should not be empty.")
self._structure = nest.map_structure(
    lambda component_spec: component_spec._unbatch(), batched_spec)  # pylint: disable=protected-access
self._name = name

batch_dim = tensor_shape.Dimension(
    tensor_shape.dimension_value(self._tensors[0].get_shape()[0]))
for t in self._tensors[1:]:
    batch_dim.assert_is_compatible_with(
        tensor_shape.Dimension(
            tensor_shape.dimension_value(t.get_shape()[0])))

variant_tensor = gen_dataset_ops.tensor_slice_dataset(
    self._tensors,
    output_shapes=structure.get_flat_tensor_shapes(self._structure),
    is_files=is_files,
    metadata=self._metadata.SerializeToString())
super().__init__(variant_tensor)
