# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/python/xla_client_backend_independent_test.py
computation = self.ExampleComputation()
hlo_dot_graph = xla_client._xla.hlo_module_to_dot_graph(
    computation.as_hlo_module())
self.assertTrue(hlo_dot_graph.startswith("digraph "))
