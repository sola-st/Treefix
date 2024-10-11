# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/composite_tensor_test.py
value = value_func()
spec = nest.map_structure(type_spec.type_spec_from_value, value,
                          expand_composites=False)
nest.assert_same_structure(value, spec, expand_composites=True)
