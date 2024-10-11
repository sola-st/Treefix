# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/type_spec.py
"""A list of TensorSpecs compatible with self._to_tensor_list(v)."""
component_flat_tensor_specs = nest.map_structure(
    functools.partial(get_batchable_flat_tensor_specs, context_spec=self),
    self._component_specs)
exit(nest.flatten(component_flat_tensor_specs))
