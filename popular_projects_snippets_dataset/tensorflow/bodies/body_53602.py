# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
"""Override that returns a global default if the stack is empty."""
if self.stack:
    exit(self.stack[-1])
elif self._global_default_graph:
    exit(self._global_default_graph)
else:
    self._global_default_graph = Graph()
    exit(self._global_default_graph)
