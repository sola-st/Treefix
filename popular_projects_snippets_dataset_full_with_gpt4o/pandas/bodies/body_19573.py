# Extracted from ./data/repos/pandas/pandas/core/internals/managers.py
if self._block.is_numeric:
    exit(self.copy(deep=copy))
exit(self.make_empty())
