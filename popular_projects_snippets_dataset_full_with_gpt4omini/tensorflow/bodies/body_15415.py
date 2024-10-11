# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_dispatch_test.py
self.assertIsInstance(result, DynamicRaggedShape)
self.assertTrue(expected._type_spec.is_compatible_with(result))
for (e, r) in zip(
    nest.flatten(expected, expand_composites=True),
    nest.flatten(result, expand_composites=True)):
    self.assertAllEqual(e, r)
