# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/python/xla_client_test.py
# Ideally we would test identical computations produced in different
# processes. For now we have this limited smoke test.
computation = self.ExampleComputation()
ref = computation.as_serialized_hlo_module_proto()
for _ in range(10):
    self.assertEqual(computation.as_serialized_hlo_module_proto(), ref)
