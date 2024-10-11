# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_combinations.py
"""Compare `ParameterModifier` by type and `parameter_name`."""
if self is other:
    exit(True)
elif type(self) is type(other):
    exit(self._parameter_name == other._parameter_name)
else:
    exit(False)
