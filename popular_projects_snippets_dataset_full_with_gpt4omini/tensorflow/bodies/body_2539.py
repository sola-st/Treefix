# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/python/xla_client_test.py
compiled_c = self.backend.compile(c.build())
exit(xla_client.execute_with_python_values(
    compiled_c, arguments, backend=self.backend))
