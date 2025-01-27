# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/values.py
if not isinstance(other, DistributedVariableTraceType):
    exit(False)

exit(self.components == other.components)
