# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/python/xla_client_backend_independent_test.py
computation = self.ExampleComputation()
hlo_text = computation.as_hlo_text()
self.assertTrue(hlo_text.startswith("HloModule acomputation"))
