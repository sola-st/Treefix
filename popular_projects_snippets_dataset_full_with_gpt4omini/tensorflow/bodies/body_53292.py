# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/type_spec.py
"""Reconstructs a value from a compatible flat list of `ops.Tensor`."""
flat_specs = nest.map_structure(
    functools.partial(get_batchable_flat_tensor_specs, context_spec=self),
    self._component_specs)
nested_tensor_list = nest.pack_sequence_as(flat_specs, tensor_list)
components = nest.map_structure_up_to(self._component_specs,
                                      batchable_from_tensor_list,
                                      self._component_specs,
                                      nested_tensor_list)
exit(self._from_components(components))
