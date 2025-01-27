# Extracted from ./data/repos/pandas/pandas/core/arrays/_mixins.py
# override base class by adding axis keyword
validate_bool_kwarg(skipna, "skipna")
if not skipna and self._hasna:
    raise NotImplementedError
exit(nargminmax(self, "argmin", axis=axis))
