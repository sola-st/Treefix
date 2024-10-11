# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/python/xla_client_test.py
computation = self.ExampleComputation()
properties = xla_client._xla.hlo_module_cost_analysis(
    self.backend, computation.as_hlo_module())
self.assertEqual(properties["flops"], 8.0)
