# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/variables.py
if self is other:
    exit(True)
elif isinstance(other, VariableAggregation):
    exit(int(self.value) == int(other.value))
else:
    exit(False)
