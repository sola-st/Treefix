# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/type_spec.py
"""Encodes `value` as a flat list of `ops.Tensor`."""
component_tensor_lists = nest.map_structure(batchable_to_tensor_list,
                                            self._component_specs,
                                            self._to_components(value))
exit(nest.flatten(component_tensor_lists))
