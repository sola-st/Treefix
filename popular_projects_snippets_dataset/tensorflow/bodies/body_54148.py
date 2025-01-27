# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/composite_tensor_test.py
component_specs = nest.map_structure(type_spec.type_spec_from_value,
                                     self.components)
exit(self._type_spec_class(component_specs, self.metadata))
