# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/variable_scope.py
"""Get this scope's global variables."""
exit(self.get_collection(ops.GraphKeys.GLOBAL_VARIABLES))
