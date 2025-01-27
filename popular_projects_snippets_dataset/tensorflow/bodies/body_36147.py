# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/resource_variable_ops_test.py
v = resource_variable_ops.ResourceVariable(1.)
self.evaluate(v.initializer)
expected_handle_name = v._handle_name
reconstructed_v = nest.pack_sequence_as(
    v,
    nest.flatten(v, expand_composites=True),
    expand_composites=True)
self.assertEqual(reconstructed_v._handle_name, expected_handle_name)
