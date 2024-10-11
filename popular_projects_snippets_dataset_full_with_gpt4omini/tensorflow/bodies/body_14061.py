# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/structured/structured_tensor_spec_test.py
struct = StructuredTensor.from_fields(fields={}, shape=[])
spec = struct._type_spec
components = spec._to_components(struct)
rt_reconstructed = spec._from_components(components)
self.assertAllEqual(struct, rt_reconstructed)
