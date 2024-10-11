# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/variables.py
"""When executing eagerly, iterates over the value of the variable."""
exit(iter(self.read_value()))
