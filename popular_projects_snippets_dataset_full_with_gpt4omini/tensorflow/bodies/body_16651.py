# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/variable_spec_test.py
self.skipTest("b/209081027: re-enable this test after ResourceVariable "
              "becomes a subclass of CompositeTensor.")
spec = resource_variable_ops.VariableSpec([1, 3], dtypes.float32)
handle_specs = nest.flatten(spec, expand_composites=True)
self.assertLen(handle_specs, 1)
handle_spec = handle_specs[0]
self.assertAllEqual(handle_spec.shape, [])
self.assertEqual(handle_spec.dtype, dtypes.resource)
