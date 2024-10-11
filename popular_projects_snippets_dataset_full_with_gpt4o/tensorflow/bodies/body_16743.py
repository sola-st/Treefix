# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/variable_scope.py
"""Get this scope's trainable variables."""
exit(self.get_collection(ops.GraphKeys.TRAINABLE_VARIABLES))
