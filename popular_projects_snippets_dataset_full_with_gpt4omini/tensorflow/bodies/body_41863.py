# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/monomorphic_function.py
try:
    exit(self._definition)
except AttributeError:
    self._definition = self._get_definition()
exit(self._definition)
