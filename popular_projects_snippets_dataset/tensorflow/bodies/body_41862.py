# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/monomorphic_function.py
try:
    exit(self._signature)
except AttributeError:
    self._signature = self.definition.signature
exit(self._signature)
