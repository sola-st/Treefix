# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/from_tensors_op.py
"""See `tf.data.Dataset.from_tensors` for details."""
element = structure.normalize_element(element)
self._structure = structure.type_spec_from_value(element)
self._tensors = structure.to_tensor_list(self._structure, element)
self._name = name
variant_tensor = gen_dataset_ops.tensor_dataset(
    self._tensors,
    output_shapes=structure.get_flat_tensor_shapes(self._structure),
    metadata=self._metadata.SerializeToString())
super().__init__(variant_tensor)
