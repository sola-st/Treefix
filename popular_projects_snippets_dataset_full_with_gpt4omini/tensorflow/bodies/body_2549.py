# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/python/xla_client_test.py
computation = self.ExampleComputation()
executable = self.backend.compile(computation)
hlo_modules = executable.hlo_modules()
self.assertLen(hlo_modules, 1)
hlo_text = hlo_modules[0].to_string()
self.assertTrue(hlo_text.startswith("HloModule acomputation"))
self.assertIn("fusion", hlo_text)
