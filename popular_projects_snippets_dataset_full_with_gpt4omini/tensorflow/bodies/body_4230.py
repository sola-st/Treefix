# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/d_variable.py
with ops.device(self._dvariable.device):
    exit(api.copy_to_mesh(t, self._original_layout))
