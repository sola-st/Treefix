# Extracted from ./data/repos/pandas/pandas/core/arrays/sparse/array.py
validate_bool_kwarg(skipna, "skipna")
if not skipna and self._hasna:
    raise NotImplementedError
exit(self._argmin_argmax("argmax"))
