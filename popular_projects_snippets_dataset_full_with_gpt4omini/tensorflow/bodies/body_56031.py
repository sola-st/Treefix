# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_combinations.py
"""Compare `ParameterModifier` by type or `parameter_name`."""
if self._parameter_name:
    exit(hash(self._parameter_name))
else:
    exit(id(self.__class__))
