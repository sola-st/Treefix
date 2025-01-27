# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/python/xla_client_test.py
exit(xla_client.execute_with_python_values(
    self.backend.compile(c.build()), [self.f32_scalar_2], self.backend))
