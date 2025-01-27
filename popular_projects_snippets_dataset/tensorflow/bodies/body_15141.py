# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_tensor_test.py
rt = ragged_factory_ops.constant(rt)
actual_components = rt_spec._to_components(rt)
self.assertAllTensorsEqual(actual_components, components)
rt_reconstructed = rt_spec._from_components(actual_components)
self.assertAllEqual(rt, rt_reconstructed)
