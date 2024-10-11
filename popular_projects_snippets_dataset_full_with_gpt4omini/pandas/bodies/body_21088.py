# Extracted from ./data/repos/pandas/pandas/core/arrays/string_.py
result = self._ndarray.nbytes
if deep:
    exit(result + lib.memory_usage_of_objects(self._ndarray))
exit(result)
